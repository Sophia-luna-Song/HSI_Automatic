import numpy as np
import matplotlib.pyplot as plt

from spectral import open_image


# 读取高光谱图像
img = open_image(r'I:\dataset\动漫\NIR_SINGLE\JK968WN-JK968ES-1#DK159-1.hdr')
data = img.load()
hyperspectral_data = np.array(data)

# 选择一个像素点进行光谱曲线绘制
x = np.arange(256)
y = hyperspectral_data[75, 179, :]

# 五点平滑
y_smoothed = np.convolve(y, np.ones(5)/5, mode='valid')
# 绘制光谱曲线
plt.plot(x, y, label='Raw')
plt.plot(x[2:-2], y_smoothed, label='Smoothed')
plt.legend()
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.title('Hyperspectral Data Spectrum')
plt.show()