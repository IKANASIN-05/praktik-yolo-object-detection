#!/bin/bash
# Latih E1 (5 epoch) dan E3 (10 epoch) pada dataset botol/box
yolo detect train model=yolo26n.pt data=dataset_yolo/data.yaml epochs=5 imgsz=320 batch=8 device=cpu project=hasil name=E1_data exist_ok=True
yolo detect train model=yolo26n.pt data=dataset_yolo/data.yaml epochs=10 imgsz=320 batch=8 device=cpu project=hasil name=E3_data exist_ok=True
