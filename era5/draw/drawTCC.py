import xarray as xr

import matplotlib.pyplot as plt
import numpy as np
import cv2

# 打开 GRIB 文件
ds = xr.open_dataset('./data/era5/data.grib', engine='cfgrib')

# 查看数据集信息

cloud_cover = ds['tcc'].values[0]
latitude = ds['latitude'].values
longitude = ds['longitude'].values

# pixel_data = np.random.rand(10, 10)
# print(pixel_data)

# 使用imshow显示像素
plt.imshow(cloud_cover, cmap='gray')
# plt.colorbar()  # 添加颜色条
plt.imsave('ttc.png', cloud_cover, cmap='gray')

plt.show()

# image_data = np.random.randint(0, 255, size=(2160, 3840, 3), dtype=np.uint8)
cv2.imwrite('4k_image.png', cloud_cover) 

ds.close()