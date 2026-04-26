import os
import json
from config import PC_DIR, INDEX_PATH

def build_index():
    index = {}
    for cls_name in os.listdir(PC_DIR):
        cls_path = os.path.join(PC_DIR, cls_name)
        if not os.path.isdir(cls_path):
            continue
        files = [os.path.join("data/point_cloud", cls_name, f) for f in os.listdir(cls_path) if f.endswith(".npy")]
        index[cls_name] = files

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"✅ 索引文件已生成：{INDEX_PATH}，共 {len(index)} 个类别")

if __name__ == "__main__":
    build_index()
