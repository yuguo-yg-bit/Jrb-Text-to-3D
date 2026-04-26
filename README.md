# JRB 3D Diffusion Engine## JRB 3D Diffusion Engine

## 中文
JRB 3D 是自研离线 3D 点云扩散引擎，全程本地运算，无需联网。输入中文即可快速生成三维模型，自动导出 STL/OBJ/GLB 格式，适配 3D 打印，支持 Python 项目嵌入与单 EXE 打包分发。
## English
JRB 3D is a self-developed offline 3D point cloud diffusion engine. All calculations are completed locally without internet. Generate 3D models through Chinese input, export STL/OBJ/GLB, support secondary development and EXE packaging.
## 日本語
JRB 3D は独自開発のオフライン 3D 点群エンジンです。ネット接続不要でローカル動作し、中国語入力で 3D モデルを作成、STL/OBJ/GLB 形式で保存できます。
## 한국어
JRB 3D는 자체 개발한 오프라인 3D 포인트 클라우드 확산 엔진입니다. 인터넷 없이 로컬 연산하며, 중국어 입력으로 3D 모델 생성, STL/OBJ/GLB 파일 출력을 지원합니다。
## Português
O JRB 3D é um motor de difusão de nuvem de pontos 3D offline desenvolvido internamente. Funciona sem internet, cria modelos 3D por texto em chinês e exporta arquivos STL, OBJ e GLB.
## ⚖️ 核心优势对比表

|对比项目|在线 AI 建模工具|JRB 3D 离线引擎|
|-------|---------------|---------------|
|网络依赖|强制联网使用|完全离线、零网络需求|
|数据隐私|文件上传云端处理|全部本地运算，隐私安全|
|使用费用|会员付费 / 次数限制|永久免费、无使用上限|
|二次开发|无法嵌入本地项目|顶层统一入口，一键嵌入 Python|
|分发方式|仅网页端访问|支持单 EXE 独立程序分发|
|模型格式|输出格式单一受限|原生支持 STL/OBJ/GLB|
📘 使用教程
## 普通用户使用
### cmd管理员/bash
运行
pip install -r requirements.txt
python main.py
运行主程序
输入中文物体名称
自动生成点云与 3D 模型
文件自动保存至 output 目录

## 开发者嵌入使用
### python
from jrb import JrbEngine

engine = JrbEngine()
res = engine.generate("立方体")

if res:
    print(res["category"])
    print(res["mesh_paths"])

-----------------------------------
📂 项目结构
plaintext
my_3d_diffusion/
├── jrb.py
├── main.py
├── config/
├── model/
├── data/
├── infer/
├── utils/
├── weights/
├── output/
├── requirements.txt
└── README.md
-------------------------------------
📦 打包指令
bash
运行
pyinstaller -F -w main.py
📜 开源协议
**JRB 3D 引擎完全自研，无闭源依赖，个人学习、二次开发、商业项目均可免费使用。**