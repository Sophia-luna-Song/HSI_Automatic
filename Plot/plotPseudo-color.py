import os
import glob
import matplotlib.pyplot as plt
from spectral import *
import numpy as np


def plotSingleImage(image_path):
    # 读取高光谱图像
    img = open_image(image_path)
    data = img.load()

    # 将第三个维度作为灰度值
    gray_data = np.mean(data, axis=2)

    # 将数据归一化到[0,1]范围内
    gray_data = (gray_data - np.min(gray_data)) / (np.max(gray_data) - np.min(gray_data))

    # 绘制伪彩色图像
    plt.imshow(gray_data, cmap='jet')
    plt.show()


def plotMultiImage(image_folder, band):
    # 获取文件路径图片
    image_files = glob.glob(os.path.join(image_folder, '*.hdr'))

    # 计算需要的子图数量
    n_images = len(image_files)
    n_cols = int(np.ceil(np.sqrt(n_images)))
    n_rows = int(np.ceil(n_images / n_cols))

    # 绘制子图
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(10, 10))
    for i, image_file in enumerate(image_files):
        # 打开图片
        img = open_image(image_file)
        data = img.load()
        gray_data = np.mean(data, axis=2)
        gray_data = (gray_data - np.min(gray_data)) / (np.max(gray_data) - np.min(gray_data))

        # 绘制子图
        row = i // n_cols
        col = i % n_cols
        axs[row, col].imshow(gray_data, cmap='jet')
        axs[row, col].set_title(os.path.basename(image_file), fontsize=6, color='red')
        axs[row, col].axis('off')

    plt.subplots_adjust(wspace=0.1, hspace=0.2)
    plt.savefig(os.path.join(image_folder, './%s.png' % band))
    plt.show()


image_folder = r'I:\动漫\VIS校正'
# band = 'All-Pseudo-color'
image_path = r'F:\dataset\动漫-花生\FXXH\RT\fuxixiaohei_RT.hdr'
plotSingleImage(image_path)
# plotMultiImage(image_folder, band)
