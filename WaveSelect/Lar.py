from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
import numpy as np


def Lar(X, y, nums=43):
    '''
           最小角回归
           X : 预测变量矩阵
           y ：标签
           nums : 选择的特征点的数目，默认为10
           return ：选择变量集的索引
    '''
    print("特征向量数：", nums)
    Lars = linear_model.Lars()
    Lars.fit(X, y)
    corflist = np.abs(Lars.coef_)

    corf = np.asarray(corflist)
    SpectrumList = corf.argsort()[-1:-(nums+1):-1]
    SpectrumList = np.sort(SpectrumList)

    model = make_pipeline(StandardScaler(with_mean=False), linear_model.Lars())  # 这里建立一个pipeline，先进行标准化，然后再进行Lars
    model.fit(X, y)
    corflist = np.abs(model.named_steps['lars'].coef_)  # 这里获取coef_的时候需要通过named_steps来获取具体的步骤

    corf = np.asarray(corflist)
    SpectrumList = corf.argsort()[-1:-(nums + 1):-1]
    SpectrumList = np.sort(SpectrumList)

    return SpectrumList