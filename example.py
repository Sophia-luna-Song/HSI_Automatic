import numpy as np
from DataLoad.DataLoad import SetSplit
from Preprocessing.Preprocessing import Preprocessing
from WaveSelect.WaveSelcet import SpctrumFeatureSelcet
from Regression.Rgs import QuantitativeAnalysis
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def SpectralQuantitativeAnalysis(data, label, ProcessMethods, FslecetedMethods, SetSplitMethods, model, windows, plsr, feature_num):

    """
    :param data: shape (n_samples, n_features), 光谱数据
    :param label: shape (n_samples, ), 光谱数据对应的标签(理化性质)
    :param ProcessMethods: string, 预处理的方法, 具体可以看预处理模块
    :param FslecetedMethods: string, 光谱波长筛选的方法
    :param SetSplitMethods : string, 划分数据集的方法
    :param model : string, 定量分析模型
    :return: Rmse: float, Rmse回归误差评估指标
             R2: float, 回归拟合,
             Mae: float, Mae回归误差评估指标
             y_pred: float, 预测值
             y_test: float, 参考值
             y_train_pred: float, 训练数据预测值
             y_train_: float, 训练数据参考值
    """
    ProcesedData = Preprocessing(ProcessMethods, data, windows)  # 预处理
    FeatrueData, labels = SpctrumFeatureSelcet(FslecetedMethods, ProcesedData, label, feature_num)  # 光谱特征选择
    # 数据集划分
    # print("特征数量：", len(FeatrueData))
    X_train, X_test, y_train, y_test = SetSplit(SetSplitMethods, FeatrueData, labels, test_size=0.2, randomseed=123)
    Rmse, R2, Mae, y_pred, y_train_pred = QuantitativeAnalysis(model, X_train, X_test, y_train, y_test, plsr)  # 定量分析
    return Rmse, R2, Mae, y_pred, y_test, y_train_pred, y_train


if __name__ == '__main__':

    data_path = r'F:\game\小论文\paper3\数据\15品种\玉米288种子MaxMin归一化光谱数据.xlsx'
    data_df = pd.read_excel(data_path, sheet_name='Sheet1', header=None)
    data = data_df.iloc[1:288, 0:256].values
    data = np.array(data)

    # 加载种子对应的油分信息
    df = pd.read_excel(r'F:\game\小论文\paper3\数据\15品种\maize288_oil.xlsx')
    # 获取第4列的数据，不包括列名
    column_data = df.iloc[0:288, 3].values
    label = np.array(column_data)
    # label = oil_content.round(6)


    Rmse_r2_mae = []
    regression_model = ["MLR"]
    preprocessing_methods = ["SG"]
    split_data_methods = ["ks"]
    feature_num = 44
    plsr = 29
    windows = 19

    for reg_model in regression_model:
        for pre_method in preprocessing_methods:
                for split_method in split_data_methods:
                    RMSE, R2, MAE, y_pred, y_test, y_train_pred, y_train = SpectralQuantitativeAnalysis(data, label, pre_method, "Lars", split_method,
                                                                         reg_model, windows, plsr, feature_num)

                    temp = [RMSE, R2, MAE, pre_method, reg_model, split_method]
                    Rmse_r2_mae.append(temp)
                    print(reg_model, pre_method, split_method, R2)
    print(Rmse_r2_mae)


    df1 = pd.DataFrame(y_train_pred)
    # 将DataFrame保存为Excel文件
    df1.to_excel('y_train_pre.xlsx', index=False)
    df2 = pd.DataFrame(y_train)
    # 将DataFrame保存为Excel文件
    df2.to_excel('y_train.xlsx', index=False)

    # 将二维数组转换为DataFrame
    df = pd.DataFrame(Rmse_r2_mae)
    # 将DataFrame保存为Excel文件
    df.to_excel('RMSE_R2_MAE_Lars_玉米15品种_MLR_SG+ks_43_num_19.xlsx', index=False)





