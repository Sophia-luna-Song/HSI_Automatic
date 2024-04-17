import numpy as np
from spectral import *
import matplotlib.pyplot as plt

# 将图像分割成等大小的块(适用于智能检测部的板子)
def seg(location):
    # 读取高光谱图像
    hyperspectral_img = open_image(location)
    bilfile = hyperspectral_img.load()
    # 读取所有波段
    data = np.array([bilfile.read_band(i) for i in range(bilfile.nbands)])
    # print(data.shape)

    increment_x = -15
    increment_y = -15

    array1 = data[:, 50 + increment_y:250 + increment_y, 50 + increment_x:310 + increment_x]
    array2 = data[:, 290 + increment_y:490 + increment_y, 50 + increment_x:310 + increment_x]
    array3 = data[:, 525 + increment_y:725 + increment_y, 50 + increment_x:310 + increment_x]

    # 存储三块种子
    array_all = []
    array_all.append(array1)
    array_all.append(array2)
    array_all.append(array3)
    array_alls = np.array(array_all)
    # 计算每个种子图像的大小
    seed_height = array1.shape[1] // 3
    seed_width = array1.shape[2] // 6

    # 初始化一个列表来保存所有的种子图像
    seeds = []
    # 将图像切割为3x6的网格
    for p in range(3):
        for i in range(3):
            for j in range(6):
                x = 0
                y = 0
                # 计算种子图像的位置
                y = i * seed_height
                x = j * seed_width

                # if p==2 and (j==1 or j==2):
                #     x = x + 5
                # # # if p==0 and (j==2 or j==3):
                # # #     x = x - 5
                # 提取种子图像，并保存到列表中
                seed = array_alls[p, :, y:y + seed_height, x:x + seed_width]
                seeds.append(seed)


    # 创建6行6列的子图
    fig, axs = plt.subplots(9, 6, figsize=(15, 10))

    for i, ax in enumerate(axs.flatten()):
        # 显示图像
        seed = seeds[i]
        ax.imshow(seed[20, :, :], cmap='gray')

        # 取消坐标轴
        ax.axis('off')

    plt.show()
    # 显示高光谱图像中的第一个波段
    plt.imshow(array1[20, :, :], cmap='gray')
    plt.axis('off')
    # 显示图
    plt.show()
    return seeds


# seg(r'I:\dataset\动漫\nir_SINGLE校正\校正\JK968WN-JK968ES-1#DK159-2_RT.hdr')