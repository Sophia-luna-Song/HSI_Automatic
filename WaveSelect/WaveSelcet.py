from WaveSelect.Lar import Lar
from WaveSelect.Spa import SPA
from WaveSelect.Uve import UVE
from WaveSelect.Cars import CARS_Cloud
from WaveSelect.Pca import Pca
from WaveSelect.GA import GA
from sklearn.model_selection import train_test_split

# ref1: 参考示例并做了修改
# ref2: https://github.com/FuSiry/OpenSA


def SpctrumFeatureSelcet(method, X, y, feature_num=30):
    """

       :param method: 波长筛选/降维的方法，包括：Cars, Lars, Uve, Spa, Pca
       :param X: 光谱数据, shape (n_samples, n_features)
       :param y: 光谱数据对应标签：格式：(n_samples，)
       :param :param y: 光谱数据对应标签：格式：(n_samples，): 预测特征数量，要进行超参数优化
       :return: X_Feature： 波长筛选/降维后的数据, shape (n_samples, n_features)
                y：光谱数据对应的标签, (n_samples，)
    """
    if method == "None":
        X_Feature = X
    elif method == "Cars":
        Featuresecletidx = CARS_Cloud(X, y)
        X_Feature = X[:, Featuresecletidx]
    elif method == "Lars":
        Featuresecletidx = Lar(X, y, nums=feature_num)
        # bands = 930+Featuresecletidx*6.32
        # print(bands)
        X_Feature = X[:, Featuresecletidx]
    elif method == "Uve":
        Uve = UVE(X, y, feature_num)
        Uve.calcCriteria()
        Uve.evalCriteria(cv=5)
        Featuresecletidx = Uve.cutFeature(X)
        X_Feature = Featuresecletidx[0]
    elif method == "Spa":
        Xcal, Xval, ycal, yval = train_test_split(X, y, test_size=0.2)
        Featuresecletidx = SPA().spa(
            Xcal=Xcal, ycal=ycal, m_min=8, m_max=50, Xval=Xval, yval=yval, autoscaling=1)
        X_Feature = X[:, Featuresecletidx]
    elif method == "GA":
        Featuresecletidx = GA(X, y)
        X_Feature = X[:, Featuresecletidx]
    elif method == "Pca":
        X_Feature = Pca(X)
    else:
        print("no this method of SpctrumFeatureSelcet!")

    return X_Feature, y