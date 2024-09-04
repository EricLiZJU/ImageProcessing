# 双边滤波
import cv2
import numpy as np

# 读取图片
image = cv2.imread('SourceImage/p1.jpg')

# 应用双边滤波
# 参数1：双边滤波器的直径，参数2：色彩空间的标准差，参数3：坐标空间的标准差
bilateral_filtered_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

# 显示结果
cv2.imwrite('SourceImage/1.jpg', bilateral_filtered_image)