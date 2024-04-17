import numpy as np
import spectral
import pandas as pd
from HSI_Automatic.Segmentation.SquareSeg import seg
import os
from PIL import ImageEnhance
import random
from scipy.ndimage import rotate


# 加载文件夹中的文件，并分割得到每个种子的立方体数据
def loadDataFolder(folder_path):

    # # 创建MinMaxScaler对象
    # scaler = MinMaxScaler()

    # 定义存储种子数据的数组
    seeds = []

    # 获取文件夹中以".hdr"为后缀的文件列表
    file_names = [file for file in os.listdir(folder_path) if file.endswith('.hdr')]

    # 遍历文件路径列表
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)  # 构建文件的完整路径
        # 调用seg()函数，并将结果添加到结果数组中
        results = seg(file_path)
        seeds.extend(results)   # results中每个元素逐个添加到seeds

    return seeds

def data_augmentation(hsi_data, oil_data, num_augmentations):
    augmented_hsi_data = []
    augmented_oil_data = []

    for i in range(len(hsi_data)):
        image = hsi_data[i]
        oil_content = oil_data[i]

        for _ in range(num_augmentations):
            # 随机裁剪
            cropped_image = random_crop(image)
            augmented_hsi_data.append(cropped_image)
            augmented_oil_data.append(oil_content)

            # 旋转
            rotated_image = random_rotation(image)
            augmented_hsi_data.append(rotated_image)
            augmented_oil_data.append(oil_content)

    return augmented_hsi_data, augmented_oil_data


def random_crop(image, crop_size=(60, 40)):
    num_channels, image_height, image_width = image.shape
    crop_height, crop_width = crop_size

    x = np.random.randint(0, image_width - crop_width + 1)
    y = np.random.randint(0, image_height - crop_height + 1)

    cropped_image = image[:, y:y + crop_height, x:x + crop_width]

    return cropped_image


def random_rotation(image):
    angle = np.random.uniform(-10, 10)
    rotated_image = rotate(image, angle, reshape=False)

    return rotated_image


def color_jitter(image):
    pil_image = spectral.imshow(image)
    enhancer = ImageEnhance.Color(pil_image)

    # 随机增强因子
    factor = random.uniform(0.8, 1.2)
    enhanced_image = enhancer.enhance(factor)

    enhanced_image = spectral.get_rgb(enhanced_image)

    return enhanced_image

## 加载高光谱图像数据集和油分含量数据集
# 加载文件夹内所有高光谱图像数据(立方体)和油分含量数据
folder_path = r'I:\dataset\动漫\nir_SINGLE校正\test'  # 高光谱图像数据，大小为(样本数, 256, X, Y)
seeds = loadDataFolder(folder_path)
hsi_data = np.array(seeds)
# print(seeds.shape)

# 加载种子对应的油分信息
df = pd.read_excel(r'F:\dataset\MRI\20230522玉米单粒油分含量.xlsx')
# 获取第4列的数据，不包括列名
column_data = df.iloc[0:270, 3].values
oil_content = np.array(column_data)
oil_data = column_data.round(6)

# 数据增强
augmented_hsi_data, augmented_oil_data = data_augmentation(hsi_data, oil_data, num_augmentations=5)
# 将增强后的数据转换为NumPy数组
augmented_hsi_data = np.array(augmented_hsi_data)
augmented_oil_data = np.array(augmented_oil_data)

print("完成")
# # 保存增强后的高光谱图像数据集和油分含量数据集
# for i in range(len(augmented_hsi_data)):
#     spectral.save_image_cube(augmented_hsi_data[i], f'augmented_hsi_data_{i}.hdr')
#     np.savetxt(f'augmented_oil_data_{i}.txt', [augmented_oil_data[i]], fmt='%.4f')