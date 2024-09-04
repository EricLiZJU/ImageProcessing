import cv2 as cv
import numpy as np
import os
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

data = [
    ['filename', 'color1', 'color1_ratio',
     'color2', 'color2_ratio',
     'color3', 'color3_ratio',
     'color4', 'color4_ratio',
     'color5', 'color5_ratio',
     'color6', 'color6_ratio',
     'color7', 'color7_ratio']
]

folder_path = 'TestImage'
file_names = os.listdir(folder_path)
file_names = [file_name for file_name in file_names if file_name != '.DS_Store']

for file_name in file_names:
    print(file_name)
    image = cv.imread('TestImage/' + file_name)
    cv.imshow("input", image)
    h, w, ch = image.shape

    # 构建图像数据
    data = image.reshape((-1, 3))
    data = np.float32(data)

    # 图像分割
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    num_clusters = 7
    ret, label, center = cv.kmeans(data, num_clusters, None, criteria, num_clusters, cv.KMEANS_RANDOM_CENTERS)

    # 生成主色彩条形卡片
    card = np.zeros((50, w, 3), dtype=np.uint8)
    clusters = np.zeros([7], dtype=np.int32)
    for i in range(len(label)):
        clusters[label[i][0]] += 1
    # 计算各类别像素的比率
    clusters = np.float32(clusters) / float(h*w)
    center = np.int32(center)
    print(center)
    x_offset = 0
    ratio = []
    total = 0
    for c in range(num_clusters):
        dx = int(clusters[c] * w)
        ratio.append(dx)
        b = center[c][0]
        g = center[c][1]
        r = center[c][2]
        cv.rectangle(card, (x_offset, 0), (x_offset+dx, 50),
                     (int(b),int(g),int(r)), -1)
        x_offset += dx
    print(ratio)
    total = sum(ratio)
    for i in range(7):
        ratio[i] = ratio[i] / total
    print(ratio)
    newdata = [file_name, center[0].tolist(), ratio[0],
               center[1].tolist(), ratio[1],
               center[2].tolist(), ratio[2],
               center[3].tolist(), ratio[3],
               center[4].tolist(), ratio[4],
               center[5].tolist(), ratio[5],
               center[6].tolist(), ratio[6]]
    print(newdata)
    #data.append(newdata)
    cv.imwrite('ColorTable/' + file_name, card)

for row in data:
    ws.append(row)

wb.save('colordata.xlsx')