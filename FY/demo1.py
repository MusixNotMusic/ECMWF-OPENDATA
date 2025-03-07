import h5py
import numpy as np
import matplotlib.pyplot as plt

# 读取HDF文件
file_path = './data/FY.HDF'
with h5py.File(file_path, 'r') as f:
    # 读取可见光、近红外和热红外通道数据
    rho_3  = f['Data/NOMChannel03'][:]  # 可见光通道反射率

    scale = f['Calibration/CALIBRATION_COEF(SCALE+OFFSET)'][:]

date_set = scale[3][0] * rho_3 + scale[3][1]

rho_G = np.clip(date_set, 0, 1)

min = np.min(rho_G)
max = np.max(rho_G)

print('max', np.max(rho_3[rho_3 < 65535]))
print('min', np.min(rho_3))


# 线性拉伸
G_out = (rho_G - min) / (max - min) * 255


# 显示云检测结果
plt.imshow(rho_G, cmap='gray')
plt.axis('off')
plt.show()