# from realesrgan import RealESRGANer
# from basicsr.archs.rrdbnet_arch import RRDBNet
import realesrgan
import cv2

# print(RRDBNet.__version__)

# 加载模型
# model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
# model_path = './models/RealESRGAN_x4plus.pth'  # 模型路径
# upsampler = RealESRGANer(
#     scale=4,
#     model_path=model_path,
#     model=model,
#     tile=0,  # 如果显存不足，可以设置 tile > 0
#     tile_pad=10,
#     pre_pad=0,
#     half=False  # 如果使用 FP16 加速，设置为 True
# )

# # 加载图像
# input_img = cv2.imread('tcc.png', cv2.IMREAD_UNCHANGED)
# if input_img is None:
#     raise ValueError('Failed to load input image!')

# # 进行超分辨率重建
# output_img, _ = upsampler.enhance(input_img)

# # 保存结果
# cv2.imwrite('output.jpg', output_img)
# print('超分辨率重建完成，结果已保存为 output.jpg')