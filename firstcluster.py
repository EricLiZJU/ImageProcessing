from skimage import io
from sklearn.cluster import KMeans
import numpy as np
import warnings
import cv2
import os


folder_path = 'TestImage'
file_names = os.listdir(folder_path)
file_names = [file_name for file_name in file_names if file_name != '.DS_Store']

for file_name in file_names:
    print(file_name)
    # 聚类个数
    k = 7
    img = cv2.imread('TestImage/' + file_name)
    # 转换数据维度
    img_ori_shape = img.shape
    img1 = img.reshape((img_ori_shape[0] * img_ori_shape[1], img_ori_shape[2]))
    img_shape = img1.shape
    # 获取图片色彩层数
    n_channels = img_shape[1]
    estimator = KMeans(n_clusters=k, max_iter=4000, init='k-means++', n_init=50)  # 构造聚类器
    estimator.fit(img1)  # 聚类
    centroids = estimator.cluster_centers_  # 获取聚类中心
    # 使用算法跑出的中心点，生成一个矩阵，为数据可视化做准备
    result = []
    result_width = 200
    result_height_per_center = 80
    for center_index in range(k):
        result.append(np.full((result_width * result_height_per_center, n_channels), centroids[center_index], dtype=int))
    result = np.array(result)
    result = result.reshape((result_height_per_center * k, result_width, n_channels))
    print(result)
    # 保存图片
    # io.imsave('TestImage/' + 'p' + file_name, result)
    print(centroids)
