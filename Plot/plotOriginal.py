import matplotlib.pyplot as plt
import spectral
import numpy as np

import re


hdr_addre = r'I:\dataset\NIR\动漫\nir_SINGLE校正\校正\120-JK968NS-JNK7286K-1_RT.hdr'
hyperspectral_img = spectral.open_image(hdr_addre)
bilfile = hyperspectral_img.load()
# spectral.imshow(bilfile)

# 读取所有波段
data = np.array([bilfile.read_band(i) for i in range(bilfile.nbands)])

# 取(z,x,y)中,x范围为(50,730),y范围为(50-310)的部分
new_array = data[:, 35:715, 35:295]


# 显示高光谱图像中的第一个波段
plt.imshow(new_array[20, :, :], cmap='gray')
plt.axis('off')
plt.show()

# Read the .hdr file content
with open(hdr_addre, 'r') as hdr_file:
    hdr_content = hdr_file.readlines()
# Extracting the wavelengths using a regular expression
wavelength_values = re.findall(r"\d+\.\d+", "\n".join(hdr_content))
wavelengths = [float(value) for value in wavelength_values]
wavelengths[:100]
selected_bands = {
    'red': 684.39,
    'green': 531.35,
    'blue': 471.57
}
# 从数据中提取红色、绿色和蓝色波段
red_band_data = data[wavelengths.index(selected_bands['red']), :, :]
green_band_data = data[wavelengths.index(selected_bands['green']), :, :]
blue_band_data = data[wavelengths.index(selected_bands['blue']), :, :]

# 将这三个波段堆叠起来，形成一个RGB图像
rgb_image_data = np.stack([red_band_data, green_band_data, blue_band_data], axis=-1)

# 归一化图像到 [0, 1] 以进行可视化
rgb_image_data_normalized = (rgb_image_data - rgb_image_data.min()) / (rgb_image_data.max() - rgb_image_data.min())

# 显示RGB图像
plt.figure(figsize=(10, 10))
plt.imshow(rgb_image_data_normalized)
plt.axis('off')
plt.title('Extracted RGB Image from provided data')
plt.show()

# 保存图像
plt.imsave('extracted_rgb_image.jpg', rgb_image_data_normalized)


# Assuming you have an image as rgb_image_data_normalized

# Define a brightness enhancement factor
enhancement_factor = 1.5

# Enhance brightness by multiplying with the enhancement factor
brightened_image = rgb_image_data_normalized * enhancement_factor

# Clip values to be in [0, 1] range
brightened_image = np.clip(brightened_image, 0, 1)

# Displaying the enhanced image
plt.figure(figsize=(10, 10))
plt.imshow(brightened_image)
plt.axis('off')
plt.title('Brightened RGB Image')
plt.show()

# If you want to save the brightened image
plt.imsave('brightened_rgb_image.png', brightened_image)

