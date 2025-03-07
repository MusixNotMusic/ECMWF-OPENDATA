import h5py
import numpy as np
import matplotlib.pyplot as plt

# 读取HDF文件
file_path = './data/FY.HDF'
with h5py.File(file_path, 'r') as f:
    # 读取可见光、近红外和热红外通道数据
    rho_B  = f['Data/NOMChannel01'][:]  # 可见光通道反射率
    rho_G  = f['Data/NOMChannel03'][:]  # 可见光通道反射率
    rho_R  = f['Data/NOMChannel02'][:]  # 近红外通道反射率

    scale = f['Calibration/CALIBRATION_COEF(SCALE+OFFSET)'][:]


rho_B = np.clip(scale[1][0] * rho_B + scale[1][1], 0, 1)
rho_G = np.clip(scale[3][0] * rho_G + scale[3][1], 0, 1)
rho_R = np.clip(scale[2][0] * rho_R + scale[2][1], 0, 1)

print('rho_G', rho_G)
print('scale', scale)

# 线性拉伸
R_out = (rho_R - np.min(rho_R)) / (np.max(rho_R) - np.min(rho_R)) * 255
G_out = (rho_G - np.min(rho_G)) / (np.max(rho_G) - np.min(rho_G)) * 255
B_out = (rho_B - np.min(rho_B)) / (np.max(rho_B) - np.min(rho_B)) * 255

# print('R_out', R_out)
# print('G_out', G_out)
# print('B_out', B_out)

# 合成RGB图像
rgb_image = np.dstack((R_out, G_out, B_out)).astype(np.uint8)

# 显示图像
plt.imshow(rgb_image)
plt.axis('off')
plt.show()