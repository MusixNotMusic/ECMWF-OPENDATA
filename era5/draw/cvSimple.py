import cv2

# 读取1K图片
img = cv2.imread('./ttc.png')

# 设置目标分辨率为4K
new_size = (3840, 2160)

# 使用双三次插值方法放大图片
resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_CUBIC)

# 保存放大后的图片
cv2.imwrite('4k_ttc_cv.jpg', resized_img)