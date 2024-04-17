import os
import numpy as np
import matplotlib.pyplot as plt


def plot_pseudo_color_image(data, band, ax, title):
    """在指定的子图轴上绘制单通道的伪彩色图像，并添加标题"""
    # 选择指定的波段
    single_band_image = data[band, :, :]

    # 归一化到[0, 1]范围
    single_band_image = (single_band_image - single_band_image.min()) / (single_band_image.max() - single_band_image.min())

    # 使用'jet'颜色映射绘制伪彩色图像
    ax.imshow(single_band_image, cmap='jet')
    # ax.set_title(title, fontsize=8)
    ax.axis('off')  # 隐藏坐标轴


def process_variety(variety_path, axes):
    """处理一个品种的所有种子，并在指定的子图中绘制伪彩色图像"""
    seed_files = sorted([os.path.join(variety_path, f) for f in os.listdir(variety_path) if f.endswith('.npy')])
    variety_name = os.path.basename(variety_path)  # 提取品种名

    # 分组种子文件
    lower_seeds = [f for f in seed_files if 1 <= int(f.split('_')[-1].split('.')[0]) <= 6]
    middle_seeds = [f for f in seed_files if 7 <= int(f.split('_')[-1].split('.')[0]) <= 12]
    upper_seeds = [f for f in seed_files if 13 <= int(f.split('_')[-1].split('.')[0]) <= 18]
    grouped_seeds = lower_seeds + middle_seeds + upper_seeds  # 按区域顺序组合

    for i, seed_file in enumerate(grouped_seeds):
        data = np.load(seed_file)
        ax = axes[i]

        # 根据种子编号确定区域
        seed_number = int(seed_file.split('_')[-1].split('.')[0])
        if seed_number <= 6:
            region = 'Lower'
        elif seed_number <= 12:
            region = 'Middle'
        else:
            region = 'Upper'

        title = f'{variety_name} - {region}'
        plot_pseudo_color_image(data, 130, ax, title)


def process_all_varieties(root_path):
    """处理所有品种，并将伪彩色图像显示在一张图中"""
    varieties = sorted([d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))])
    max_seeds = max(len(os.listdir(os.path.join(root_path, v))) for v in varieties)
    fig, axes = plt.subplots(len(varieties), max_seeds, figsize=(max_seeds * 2, len(varieties) * 2))

    for variety_index, variety in enumerate(varieties):
        variety_path = os.path.join(root_path, variety)
        process_variety(variety_path, axes[variety_index])

    plt.tight_layout()
    plt.show()

# 调用函数
root_path = 'F:\game\小论文\paper3\数据\玉米种子高光谱图像部分伪彩图展示\玉米种子光谱图像'
process_all_varieties(root_path)
