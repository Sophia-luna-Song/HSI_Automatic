import pandas as pd
import numpy as np
from DataLoad.DataLoad import SetSplit
from Preprocessing.Preprocessing import Preprocessing
from WaveSelect.WaveSelcet import SpctrumFeatureSelcet
from Regression.Rgs import QuantitativeAnalysis
import warnings
warnings.filterwarnings('ignore')


# 光谱定量分析
def SpectralQuantitativeAnalysis(data, label, ProcessMethods, FslecetedMethods, SetSplitMethods, model, feature_num, window, pls_num=8):

    ProcesedData = Preprocessing(ProcessMethods, data, window)    # 预处理
    FeatrueData, labels = SpctrumFeatureSelcet(FslecetedMethods, ProcesedData, label, feature_num)    # 光谱特征选择
    X_train, X_test, y_train, y_test = SetSplit(SetSplitMethods, FeatrueData, labels, test_size=0.2, randomseed=123)
    Rmse, R2, Mae, y_pred = QuantitativeAnalysis(model, X_train, X_test, y_train, y_test, pls_num)    # 定量分析
    return Rmse, R2, Mae, y_pred


if __name__ == '__main__':

    data_path = r'F:\game\小论文\paper3\数据\15品种\玉米287种子MaxMin归一化光谱数据.xlsx'
    data_df = pd.read_excel(data_path, sheet_name='Sheet1', header=None)
    data = data_df.iloc[1:, :].values
    data = np.array(data)


    # 加载种子对应的油分信息
    df = pd.read_excel(r'F:\game\小论文\paper3\数据\15品种\maize287_oil.xlsx')
    # 获取第4列的数据，不包括列名
    column_data = df.iloc[0:288, 3].values
    label = np.array(column_data)


    # 循环100次独立实验，查看各方法得到的R2等参数的稳定性
    Rmse_r2_mae = []
    regression_model = ["Pls"]
    preprocessing_methods = ["SG"]
    split_data_methods = ["ks"]
    for reg_model in regression_model:
        for pre_method in preprocessing_methods:
            for num in range(10, 100):
                for window in range(5, 20):
                    for split_method in split_data_methods:
                        if num > 30:
                            pls_nums = 30
                        else:
                            pls_nums = num
                            for pls_num in range(8, pls_nums):
                                RMSE, R2, MAE, y_pred = SpectralQuantitativeAnalysis(data, label, pre_method, "Lars",
                                                                                 split_method,
                                                                                 reg_model, num, window, pls_num)

                                temp = [RMSE, R2, MAE, pre_method, reg_model, split_method, num, window, pls_num]
                                Rmse_r2_mae.append(temp)
                                print(reg_model, pre_method, split_method, R2, num, window)
    print(Rmse_r2_mae)


    # 将二维数组转换为DataFrame
    df = pd.DataFrame(Rmse_r2_mae)

    # 将DataFrame保存为Excel文件
    df.to_excel('RMSE_R2_MAE_Lars_best_num_玉米——PLSR(动态回归数_1).xlsx', index=False)