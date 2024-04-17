from Segmentation import SquareSeg
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
from Preprocessing.normalize_data import normalize_data

"""
从原始高光谱图像中，将54*3的种子分割成单独的种子，并利用第20个波段二值化处理，并利用膨胀操作优化后获取ROI，然后计算平均光谱后输出到excel表格中
"""


def roi(location, band):
    seeds = SquareSeg.seg(location)
    seeds = np.array(seeds)

    # 获取第20个波段
    band_num = seeds[:, band, :, :]

    # # 对第20个波段进行中值滤波平滑处理(效果不好)
    # med = median(band20)

    # 进行二值化处理，将背景设为0，玉米种子设为1
    thresh = threshold_otsu(band_num)
    binary = np.zeros_like(band_num)
    binary[band_num > thresh] = 1

    # 膨胀操作优化感兴趣区域
    kernel = np.ones((1, 1), np.uint8)
    dilated_binary = cv2.dilate(binary.astype(np.uint8), kernel, iterations=1)
    dilated_binary = 1 - dilated_binary

    # 设置绘图
    fig, axes = plt.subplots(nrows=9, ncols=6, figsize=(18, 12))  # 创建6x9的子图网格
    axes = axes.flatten()

    # 在子图中绘制每个种子的二值化图像
    for i in range(54):
        axes[i].imshow(dilated_binary[i], cmap='binary')  # 使用二值颜色映射显示图像
        axes[i].axis('off')  # 关闭坐标轴

    # 调整子图间距
    plt.tight_layout()
    plt.show()

    # 提取ROI
    rois = []
    for i in range(54):
        roi = np.zeros_like(seeds[i])   # 创建一个与原始图像相同大小的全0数组作为输出图像
        seed = seeds[i]
        roi[:, dilated_binary[i] == 1] = seed[:, dilated_binary[i] == 1]
        rois.append(roi)


    # 初始化一个二维数组
    avg_spectras = []
    for i in range(54):
        # 初始化一个空的数组用于存储每个波段的平均值
        avg_spectra = np.zeros(256)
        for j in range(256):
            # 为了计算非零像素的平均值，我们需要找到那些非零像素
            roi = rois[i]
            non_zero_pixels = roi[j, :, :][roi[j, :, :] != 0]
            if non_zero_pixels.size > 0:
                avg_spectra[j] = np.mean(non_zero_pixels)
        avg_spectras.append(avg_spectra)
        # print(avg_spectra)  # 打印256个波段的平均光谱值

    # 创建9行6列的子图
    fig, axs = plt.subplots(9, 6, figsize=(15, 10))

    for i, ax in enumerate(axs.flatten()):
        # 显示图像
        roi = rois[i]
        ax.imshow(roi[20, :, :], cmap='gray')
        # 添加矩形边界框
        binary_roi = dilated_binary[i]
        contours, _ = cv2.findContours(binary_roi.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            rect = plt.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
        # 取消坐标轴
        ax.axis('off')
        # print(1)
    plt.show()

    return avg_spectras, rois



def main():
    location = r'I:\dataset\NIR\动漫\nir_SINGLE校正\校正\120-JK968NS-JNK7286K-1_RT.hdr'
    band = 30
    avg_spectras, rois = roi(location, band)

    df = pd.DataFrame(avg_spectras)
    # 将DataFrame保存为Excel文件
    df.to_excel(f'F:\dataset\\test1.xlsx', index=False)


if __name__ == '__main__':
    main()