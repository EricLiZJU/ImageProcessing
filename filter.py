# 双边滤波

import cv2
import os
import numpy as np

folder_path = 'SourceImage'
file_names = os.listdir(folder_path)
file_names = [file_name for file_name in file_names if file_name != '.DS_Store']

for file_name in file_names:
    print(file_name)

    # 读取图片
    image = cv2.imread('SourceImage/' + file_name)

    # 应用双边滤波
    # 参数1：双边滤波器的直径，参数2：色彩空间的标准差，参数3：坐标空间的标准差
    bilateral_filtered_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

    # 显示结果
    cv2.imwrite('FiltedImage/' + file_name, bilateral_filtered_image)
