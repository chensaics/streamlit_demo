# 用streamlit实现一个FasterRCNN的网页交互APP范例。
# 为了便于向合作伙伴展示我们的模型App,可以将stremlit的模型部署到 HuggingFace的 Space托管空间中，完全免费的哦。
# 方法如下：
# 1，注册huggingface账号：https://huggingface.co/join
# 2，在space空间中创建项目：https://huggingface.co/spaces
# start new space ===> 选择 SDK streamlit
# 3，创建好的项目有一个Readme文档，根据说明操作即可。

import numpy as np
from PIL import Image, ImageColor, ImageDraw, ImageFont
import torch
from torch import nn
import torchvision
from torchvision import datasets, models, transforms

import streamlit as st


# 可视化函数
def plot_detection(image, prediction, idx2names, min_score=0.8):
    image_result = image.copy()
    boxes, labels, scores = prediction['boxes'], prediction['labels'], prediction['scores']
    draw = ImageDraw.Draw(image_result)
    for idx in range(boxes.shape[0]):
        if scores[idx] >= min_score:
            x1, y1, x2, y2 = boxes[idx][0], boxes[idx][1], boxes[idx][2], boxes[idx][3]
            name = idx2names.get(str(labels[idx].item()))
            score = scores[idx]
            draw.rectangle((x1, y1, x2, y2), fill=None, outline='lawngreen', width=2)
            draw.text((x1, y1), name + ":\n" + str(round(score.item(), 2)), fill="red")
    return image_result


# 加载模型
@st.cache()
def load_model():
    num_classes = 91
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True, num_classes=num_classes)
    if torch.cuda.is_available():
        model.to("cuda:0")
    model.eval()
    model.idx2names = {'0': 'background', '1': 'person', '2': 'bicycle', '3': 'car',
                       '4': 'motorcycle', '5': 'airplane', '6': 'bus', '7': 'train', '8': 'truck', '9': 'boat',
                       '10': 'traffic light', '11': 'fire hydrant', '13': 'stop sign',
                       '14': 'parking meter', '15': 'bench', '16': 'bird', '17': 'cat',
                       '18': 'dog', '19': 'horse', '20': 'sheep', '21': 'cow', '22': 'elephant',
                       '23': 'bear', '24': 'zebra', '25': 'giraffe', '27': 'backpack',
                       '28': 'umbrella', '31': 'handbag', '32': 'tie', '33': 'suitcase',
                       '34': 'frisbee', '35': 'skis', '36': 'snowboard', '37': 'sports ball',
                       '38': 'kite', '39': 'baseball bat', '40': 'baseball glove', '41': 'skateboard',
                       '42': 'surfboard', '43': 'tennis racket', '44': 'bottle', '46': 'wine glass',
                       '47': 'cup', '48': 'fork', '49': 'knife', '50': 'spoon', '51': 'bowl',
                       '52': 'banana', '53': 'apple', '54': 'sandwich', '55': 'orange',
                       '56': 'broccoli', '57': 'carrot', '58': 'hot dog', '59': 'pizza',
                       '60': 'donut', '61': 'cake', '62': 'chair', '63': 'couch',
                       '64': 'potted plant', '65': 'bed', '67': 'dining table',
                       '70': 'toilet', '72': 'tv', '73': 'laptop', '74': 'mouse',
                       '75': 'remote', '76': 'keyboard', '77': 'cell phone',
                       '78': 'microwave', '79': 'oven', '80': 'toaster',
                       '81': 'sink', '82': 'refrigerator', '84': 'book',
                       '85': 'clock', '86': 'vase', '87': 'scissors',
                       '88': 'teddybear', '89': 'hair drier', '90': 'toothbrush'}
    return model


def predict_detection(model, image_path, min_score=0.8):
    # 准备数据
    inputs = []
    img = Image.open(image_path).convert("RGB")
    img_tensor = torch.from_numpy(np.array(img) / 255.).permute(2, 0, 1).float()
    if torch.cuda.is_available():
        img_tensor = img_tensor.cuda()
    inputs.append(img_tensor)

    # 预测结果
    with torch.no_grad():
        predictions = model(inputs)

    # 结果可视化
    img_result = plot_detection(img, predictions[0],
                                model.idx2names, min_score=min_score)
    return img_result


st.title("FasterRCNN功能演示")

st.header("FasterRCNN Input:")
image_file = st.file_uploader("upload a image file(jpg/png) to predict:")
if image_file is not None:
    try:
        st.image(image_file)
    except Exception as err:
        st.write(err)
else:
    image_file = "horseman.png"
    st.image(image_file)

min_score = st.slider(label="choose the min_score parameter:", min_value=0.1, max_value=0.98, value=0.8)

st.header("FasterRCNN Prediction:")
with st.spinner('waitting for prediction...'):
    model = load_model()
    img_result = predict_detection(model, image_file, min_score=min_score)
    st.image(img_result)








