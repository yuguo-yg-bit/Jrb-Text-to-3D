import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from config import PC_DIR, INDEX_PATH, NUM_POINTS, BATCH_SIZE

class PointCloudDataset(Dataset):
    def __init__(self):
        # 读取索引
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            self.index = json.load(f)

        self.items = []
        total_classes = len(self.index)
        total_files = 0
        for cls_name, paths in self.index.items():
            total_files += len(paths)

        print(f"=" * 60)
        print(f"📂 数据集总览：{total_classes} 个类别 | {total_files} 个点云文件")
        print(f"=" * 60)

        # 遍历所有文件，带实时打印
        current = 0
        for cls_name, path_list in self.index.items():
            for rel_path in path_list:
                current += 1
                abs_path = os.path.abspath(
                    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), rel_path)
                )

                # ✅ 实时打印正在处理的文件
                print(f"[{current}/{total_files}] 正在加载：{cls_name} | {abs_path}")

                self.items.append((cls_name, abs_path))

        print(f"\n✅ 全部加载完成！共 {len(self.items)} 个有效样本\n")

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        cls_name, file_path = self.items[idx]

        # 读取点云
        pc = np.load(file_path)
        pc = pc.astype(np.float32)

        # 标准化
        center = np.mean(pc, axis=0)
        pc = pc - center
        max_dist = np.max(np.linalg.norm(pc, axis=1))
        if max_dist > 1e-8:
            pc = pc / max_dist

        # 固定点数
        if pc.shape[0] >= NUM_POINTS:
            pc = pc[:NUM_POINTS]
        else:
            pad = NUM_POINTS - pc.shape[0]
            pc = np.concatenate([pc, pc[-pad:]], axis=0)

        return torch.from_numpy(pc), cls_name

def get_dataloader():
    dataset = PointCloudDataset()
    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=0,
        drop_last=True
    )
    return loader