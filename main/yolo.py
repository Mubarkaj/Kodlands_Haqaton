from roboflow import Roboflow
rf = Roboflow(api_key="API_KEY")
project = rf.workspace("mubarmajs-workspace").project("trash-can-blbnr-cruqc")
version = project.version(1)
dataset = version.download("yolov8")