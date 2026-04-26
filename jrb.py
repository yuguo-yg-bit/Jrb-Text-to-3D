import os
import sys

# ==============================
# 官方引擎核心类：Jrb3dEngine
# 开发者标准调用：from jrb import Jrb3dEngine
# ==============================
class Jrb3dEngine:
    def __init__(self):
        # 引擎根目录
        self.ROOT = os.path.dirname(os.path.abspath(__file__))
        
        # 核心目录定义
        self.DATA_DIR = os.path.join(self.ROOT, "data")
        self.POINT_CLOUD_DIR = os.path.join(self.DATA_DIR, "point_cloud")
        self.MODEL_DIR = os.path.join(self.ROOT, "model")
        self.INFER_DIR = os.path.join(self.ROOT, "infer")
        self.WEIGHTS_DIR = os.path.join(self.ROOT, "weights")
        self.OUTPUT_DIR = os.path.join(self.ROOT, "output")

        # 自动创建必要文件夹
        self._build_dirs()

    def _build_dirs(self):
        """自动创建目录"""
        for d in [
            self.WEIGHTS_DIR,
            self.OUTPUT_DIR,
            self.POINT_CLOUD_DIR
        ]:
            os.makedirs(d, exist_ok=True)

    def get_save_path(self, filename):
        """获取输出文件路径"""
        return os.path.join(self.OUTPUT_DIR, filename)

    def get_weight_path(self, filename):
        """获取权重文件路径"""
        return os.path.join(self.WEIGHTS_DIR, filename)

    def get_category_folder(self, category_name):
        """获取分类数据集路径"""
        return os.path.join(self.POINT_CLOUD_DIR, category_name)

# ==============================
# 全局单例（供内部快速调用）
# ==============================
engine = Jrb3dEngine()