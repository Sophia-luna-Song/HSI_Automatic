import os
import numpy as np
import matplotlib.pyplot as plt

def average_spectral_cube(seed_files):
    """计算种子的平均光谱立方体"""
    cubes = [np.load(file) for file in seed_files]
    return np.mean(cubes, axis=0)

def plot_pseudo_color_image(data, bands, ax, title):
    """在指定的子图轴上绘制伪彩色图像，并添加标题"""
    rgb_image = data[bands, :, :]
    # 将颜色通道移动到最后一个维度
    rgb_image = np.transpose(rgb_image, (1, 2, 0))
    rgb_image = (rgb_image - rgb_image.min()) / (rgb_image.max() - rgb_image.min())
    ax.imshow(rgb_image, cmap='jet')
    # ax.set_title(title)
    ax.axis('off')  # 隐藏坐标轴

def process_variety(variety_path, variety_name):
    """处理一个品种的所有种子，并绘制伪彩色图像"""
    seed_files = [os.path.join(variety_path, f) for f in os.listdir(variety_path) if f.endswith('.npy')]

    lower_seeds = [f for f in seed_files if 1 <= int(f.split('_')[-1].split('.')[0]) <= 6]
    middle_seeds = [f for f in seed_files if 7 <= int(f.split('_')[-1].split('.')[0]) <= 12]
    upper_seeds = [f for f in seed_files if 13 <= int(f.split('_')[-1].split('.')[0]) <= 18]

    lower_avg_cube = average_spectral_cube(lower_seeds)
    middle_avg_cube = average_spectral_cube(middle_seeds)
    upper_avg_cube = average_spectral_cube(upper_seeds)

    bands = [130]
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    plot_pseudo_color_image(lower_avg_cube, bands, axes[2], f'{variety_name} - 下部')
    plot_pseudo_color_image(middle_avg_cube, bands, axes[1], f'{variety_name} - 中部')
    plot_pseudo_color_image(upper_avg_cube, bands, axes[0], f'{variety_name} - 上部')

    plt.tight_layout()
    plt.show()
    plt.close(fig)  # 关闭当前图形窗口

def process_all_varieties(root_path):
    """处理所有品种，并为每个品种显示一个图像"""
    varieties = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]
    for variety in varieties:
        variety_path = os.path.join(root_path, variety)
        process_variety(variety_path, variety)

# 调用函数
root_path = 'F:\game\小论文\paper3\数据\玉米种子光谱图像'
process_all_varieties(root_path)
