# 加载预训练模型并处理图像
import torch
import torch.nn as nn
import cv2
import numpy as np
from torchvision.transforms.functional import to_tensor, to_pil_image

model_url = './models/RRDB_ESRGAN_x4.pth'

# 定义模型架构（假设你有一个定义好的模型类）
class RRDB_ESRGAN_x4(nn.Module):
    def __init__(self):
        super(RRDB_ESRGAN_x4, self).__init__()
        # 定义模型层
        pass

    def forward(self, x):
        # 定义前向传播
        pass

# 加载模型
model = RRDB_ESRGAN_x4()
model.load_state_dict(torch.load(model_url))
model.eval()

# 读取1K图片
img = cv2.imread('./ttc.png')

# 确保图像不是空的
if img is None:
    raise ValueError("Image not found or unable to load.")

# 将图像从 BGR 转换为 RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 转换为张量并归一化
img_tensor = to_tensor(img).unsqueeze(0)

# 使用模型放大图片
with torch.no_grad():
    resized_img_tensor = model(img_tensor)

# 反归一化并转换为 PIL 图像
resized_img = to_pil_image(resized_img_tensor.squeeze(0).clamp(0, 1))

# 保存放大后的图片
resized_img.save('4k_ttc_sm.jpg')