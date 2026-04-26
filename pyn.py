import numpy as np

# 替换成你自己的 .npy 文件路径
npy_path = "data/point_cloud/adjustment_screw/sample_01.npy"

# 读取文件
points = np.load(npy_path)

# 打印基础信息
print("点云形状:", points.shape)       # 正常应为 (N, 3)，比如 (2048, 3)
print("数据类型:", points.dtype)      # 正常应为 float32 / float64
print("坐标范围:")
print("  X轴:", points[:, 0].min(), "~", points[:, 0].max())
print("  Y轴:", points[:, 1].min(), "~", points[:, 1].max())
print("  Z轴:", points[:, 2].min(), "~", points[:, 2].max())
print("是否有 NaN:", np.isnan(points).any())
print("是否有 Inf:", np.isinf(points).any())
