import matplotlib.pyplot as plt
from spectral import envi, view_cube, settings
settings.WX_GL_DEPTH_SIZE = 16
import pandas as pd


# 显示图像
def plotspc(data, format):
    if format == "original image":
        plt = plotOriginalImage(data)
    elif format == "raw specturm":
        plt = plotSpectrum(data)
    else:
        print("no this model of QuantitativeAnalysis")
    return plt


# 显示原图像 空白!!
def plotOriginalImage(data_addr):

    img = envi.open(data_addr)
    arr = view_cube(img, bands=[29, 19, 9])
    plt.pause(60)


# 显示光谱曲线
def plotSpectrum(spec, title, x=930, fwhm=None):
    """
       :param spec: shape (n_samples, n_features)
       :param fwhm: list of spectral resolutions for each wavelength
       :return: plt
    """
    colors = [
        '#FF0000',  # 红色
        '#FFA500',  # 橙色
        '#FFFF00',  # 黄色
        '#008000',  # 绿色
        '#00FFFF',  # 青色
        '#0000FF',  # 蓝色
        '#800080',  # 紫色
        '#A52A2A',  # 棕色
        '#FFC0CB',  # 粉色
        '#808080',  # 灰色
        '#000000',  # 黑色
        '#90EE90',  # 浅绿色
        '#D2B48C',  # 浅棕色（棕褐色）
        '#98FB98',  # 浅绿色
        '#ADD8E6'   # 浅蓝色
    ]

    spec = pd.DataFrame(spec)
    if isinstance(spec, pd.DataFrame):
        spec = spec.values
        spec = spec[:, :(spec.shape[1] - 1)]
        plt.rcParams['font.family'] = 'Times New Roman'   # 正常显示英文
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        wl = [x + sum(fwhm[:i]) for i in range(len(fwhm))]  # Calculate wavelengths based on fwhm
        with plt.style.context(('seaborn-bright')):
            fonts = 16
            plt.figure(figsize=(10, 6), dpi=100)
            for i in range(min(15, spec.shape[0])):  # 限制最多显示15条线
                plt.plot(wl, spec[i, :].T, label=f'Line {i + 1}', color=colors[i])
            plt.xlabel('Wavelength (nm)', fontsize=fonts)
            plt.ylabel('Reflectance', fontsize=fonts)
            plt.title(title, fontsize=fonts)
            plt.legend()
        return plt