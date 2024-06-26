import pandas as pd
import numpy as np
from Preprocessing.Preprocessing import Preprocessing
from Plot.PlotSpectral import plotSpectrum
import matplotlib.ticker as ticker


def main():
    fwhm = {
        6.184755,
        6.186004,
        6.187254,
        6.188504,
        6.189754,
        6.191003,
        6.192253,
        6.193503,
        6.194753,
        6.196002,
        6.197252,
        6.198502,
        6.199752,
        6.201001,
        6.202251,
        6.203501,
        6.204751,
        6.206000,
        6.207250,
        6.208500,
        6.209749,
        6.210999,
        6.212249,
        6.213499,
        6.214748,
        6.215998,
        6.217248,
        6.218498,
        6.219747,
        6.220997,
        6.222247,
        6.223497,
        6.224746,
        6.225996,
        6.227246,
        6.228496,
        6.229745,
        6.230995,
        6.232245,
        6.233495,
        6.234744,
        6.235994,
        6.237244,
        6.238494,
        6.239743,
        6.240993,
        6.242243,
        6.243493,
        6.244742,
        6.245992,
        6.247242,
        6.248492,
        6.249741,
        6.250991,
        6.252241,
        6.253491,
        6.254740,
        6.255990,
        6.257240,
        6.258489,
        6.259739,
        6.260989,
        6.262239,
        6.263488,
        6.264738,
        6.265988,
        6.267238,
        6.268487,
        6.269737,
        6.270987,
        6.272237,
        6.273486,
        6.274736,
        6.275986,
        6.277236,
        6.278485,
        6.279735,
        6.280985,
        6.282235,
        6.283484,
        6.284734,
        6.285984,
        6.287234,
        6.288483,
        6.289733,
        6.290983,
        6.292233,
        6.293482,
        6.294732,
        6.295982,
        6.297232,
        6.298481,
        6.299731,
        6.300981,
        6.302231,
        6.303480,
        6.304730,
        6.305980,
        6.307229,
        6.308479,
        6.309729,
        6.310979,
        6.312228,
        6.313478,
        6.314728,
        6.315978,
        6.317227,
        6.318477,
        6.319727,
        6.320977,
        6.322226,
        6.323476,
        6.324726,
        6.325976,
        6.327225,
        6.328475,
        6.329725,
        6.330975,
        6.332224,
        6.333474,
        6.334724,
        6.335974,
        6.337223,
        6.338473,
        6.339723,
        6.340973,
        6.342222,
        6.343472,
        6.344722,
        6.345972,
        6.347221,
        6.348471,
        6.349721,
        6.350971,
        6.352220,
        6.353470,
        6.354720,
        6.355969,
        6.357219,
        6.358469,
        6.359719,
        6.360968,
        6.362218,
        6.363468,
        6.364718,
        6.365967,
        6.367217,
        6.368467,
        6.369717,
        6.370966,
        6.372216,
        6.373466,
        6.374716,
        6.375965,
        6.377215,
        6.378465,
        6.379715,
        6.380964,
        6.382214,
        6.383464,
        6.384714,
        6.385963,
        6.387213,
        6.388463,
        6.389713,
        6.390962,
        6.392212,
        6.393462,
        6.394712,
        6.395961,
        6.397211,
        6.398461,
        6.399711,
        6.400960,
        6.402210,
        6.403460,
        6.404709,
        6.405959,
        6.407209,
        6.408459,
        6.409708,
        6.410958,
        6.412208,
        6.413458,
        6.414707,
        6.415957,
        6.417207,
        6.418457,
        6.419706,
        6.420956,
        6.422206,
        6.423456,
        6.424705,
        6.425955,
        6.427205,
        6.428455,
        6.429704,
        6.430954,
        6.432204,
        6.433454,
        6.434703,
        6.435953,
        6.437203,
        6.438453,
        6.439702,
        6.440952,
        6.442202,
        6.443452,
        6.444701,
        6.445951,
        6.447201,
        6.448451,
        6.449700,
        6.450950,
        6.452200,
        6.453449,
        6.454699,
        6.455949,
        6.457199,
        6.458448,
        6.459698,
        6.460948,
        6.462198,
        6.463447,
        6.464697,
        6.465947,
        6.467197,
        6.468446,
        6.469696,
        6.470946,
        6.472196,
        6.473445,
        6.474695,
        6.475945,
        6.477195,
        6.478444,
        6.479694,
        6.480944,
        6.482194,
        6.483443,
        6.484693,
        6.485943,
        6.487193,
        6.488442,
        6.489692,
        6.490942,
        6.492192,
        6.493441,
        6.494691,
        6.495941,
        6.497191,
        6.498440,
        6.499690,
        6.500940,
        6.502189,
        6.502189
    }
    data_path = r'F:\game\小论文\paper3\数据\15品种\玉米288传统方法获取平均光谱.xlsx'
    data_df = pd.read_excel(data_path, sheet_name='Sheet1', header=None)
    data = data_df.iloc[1:288, 0:256].values
    data = np.array(data)
    x = 930.789605
    fwhm_list = list(fwhm)
    plt1 = plotSpectrum(data, title="Original Spectrum", x=x, fwhm=fwhm_list)
    plt1.grid(True)
    plt1.gca().xaxis.set_major_locator(ticker.MultipleLocator(50))
    plt1.show()

    preprocessing_methods = ["SG", "MA", "WAVE", "D2", "D1", "MSC", "None"]
    for pre_method in preprocessing_methods:
        pre_data = Preprocessing(pre_method, data)
        plt2 = plotSpectrum(pre_data, title=pre_method)
        plt1.grid(True)
        plt1.gca().xaxis.set_major_locator(ticker.MultipleLocator(50))
        plt2.show()



if __name__ == '__main__':
    main()