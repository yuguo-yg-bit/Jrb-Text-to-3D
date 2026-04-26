import os

# 路径
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")
PC_DIR = os.path.join(DATA_DIR, "point_cloud")
INDEX_PATH = os.path.join(DATA_DIR, "dataset_index.json")
WEIGHTS_DIR = os.path.join(ROOT_DIR, "weights")
os.makedirs(WEIGHTS_DIR, exist_ok=True)

# 点云配置
NUM_POINTS = 2048
POINT_DIM = 3


# 文本编码
TEXT_DIM = 512

# 扩散参数
TIMESTEPS = 1000
BETA_START = 0.0001
BETA_END = 0.02

# 训练超参
BATCH_SIZE = 8
EPOCHS = 200
LEARNING_RATE = 1e-4
SAVE_INTERVAL = 10

# 设备
import torch
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
OUTPUT_DIR="outputs"