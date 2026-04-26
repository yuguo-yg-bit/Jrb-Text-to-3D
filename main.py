import os
import torch
from config import DEVICE, WEIGHTS_DIR, NUM_POINTS
from model.text_encoder import IndustrialTextEncoder as TextEncoder
from model.diffusion_3d import Diffusion3D
from model.mesh_recon import MeshReconstructor
from infer.generate_3d import export_3d_model

# ----------------------
# 全局模型加载
# ----------------------
text_encoder = TextEncoder().to(DEVICE)
diffusion_model = Diffusion3D().to(DEVICE)
mesh_recon = MeshReconstructor()

# ----------------------
# 【安全模式：权重加载失败就跳过】
# ----------------------
def load_latest_weights():
    try:
        if not os.path.exists(WEIGHTS_DIR):
            print("⚠️ 权重文件夹不存在，使用初始化模型")
            return
            
        weight_files = [f for f in os.listdir(WEIGHTS_DIR) if f.endswith((".pth", ".pt"))]
        if not weight_files:
            print("⚠️ 未找到权重文件，使用初始化模型")
            return
            
        latest = sorted(weight_files)[-1]
        path = os.path.join(WEIGHTS_DIR, latest)
        ckpt = torch.load(path, map_location=DEVICE)
        
        # 安全加载，不匹配就跳过
        diffusion_model.load_state_dict(ckpt, strict=False)
        print(f"✅ 模型已启动（权重兼容模式）")
    except:
        print("✅ 3D引擎已启动（使用初始化模型）")

# 执行
load_latest_weights()
diffusion_model.eval()

# ----------------------
# 核心：文字 → 3D 点云
# ----------------------
@torch.no_grad()
def text_to_3d(text: str):
    print(f"\n输入文本：{text}")
    print(" 文本编码中...")
    
    text_feat = text_encoder.encode_single(text)
    text_feat = text_feat[0] if isinstance(text_feat, tuple) else text_feat
    text_feat = text_feat.to(DEVICE).unsqueeze(0)

    print("🔹 3D扩散模型生成点云中...")
    point_cloud = diffusion_model.sample(text_feat, DEVICE)
    point_cloud = point_cloud.squeeze(0).cpu().numpy()
    print(f"✅ 点云生成完成：{point_cloud.shape}")
    return point_cloud

# ----------------------
# 主程序
# ----------------------
if __name__ == "__main__":
    print("=" * 50)
    print("    自研 3D AI 引擎 · 文字生成3D模型")
    print("=" * 50)

    while True:
        print("\n请输入你想生成的物体（输入 exit 退出）：")
        user_input = input("> ")

        if user_input.lower() in ["exit", "quit", "q"]:
            print("👋 退出程序")
            break

        if not user_input.strip():
            print("⚠️  输入不能为空")
            continue

        pc = text_to_3d(user_input)

        print("\n🔹 开始导出 3D 模型...")
        export_3d_model(
            points=pc,
            text_prompt=user_input,
            recon=mesh_recon
        )
