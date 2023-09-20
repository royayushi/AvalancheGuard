from ultralytics import YOLO


model = YOLO("yolov8n.yaml") 

# Use the model
model.train(data="config.yaml", epochs=1)
