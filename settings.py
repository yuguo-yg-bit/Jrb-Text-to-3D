import os

# Project root path
PROJECT_ROOT = os.path.abspath(".")

# Data path config
DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")
POINT_CLOUD_ROOT = os.path.join(DATA_FOLDER, "point_cloud")
CATEGORY_MAP_PATH = os.path.join(DATA_FOLDER, "category_map.json")

# Model weights path
WEIGHTS_FOLDER = os.path.join(PROJECT_ROOT, "weights")
DIFFUSION_WEIGHT_PATH = os.path.join(WEIGHTS_FOLDER, "diffusion_weight.pt")
TEXT_EMBED_PATH = os.path.join(WEIGHTS_FOLDER, "text_embed.npy")

# Output format path
OUTPUT_FOLDER = os.path.join(PROJECT_ROOT, "output")
OUTPUT_STL = os.path.join(OUTPUT_FOLDER, "stl")
OUTPUT_OBJ = os.path.join(OUTPUT_FOLDER, "obj")
OUTPUT_GLB = os.path.join(OUTPUT_FOLDER, "glb")

# Point cloud basic params
POINT_NUM = 2048
TEXT_EMBED_DIM = 128
CLASS_NUM = 300

# Create necessary directories
os.makedirs(OUTPUT_STL, exist_ok=True)
os.makedirs(OUTPUT_OBJ, exist_ok=True)
os.makedirs(OUTPUT_GLB, exist_ok=True)
os.makedirs(WEIGHTS_FOLDER, exist_ok=True)