
from sklearn.cross_decomposition import PLSRegression
import hpelm
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from Evaluate.RgsEvaluate import ModelRgsevaluate

# ref1: 参考示例并做了修改
# ref2: https://github.com/FuSiry/OpenSA


# 最小二乘
def Pls(X_train, X_test, y_train, y_test, num=8):
    print("偏最小二乘主成分：", num)
    model = PLSRegression(n_components=num)
    # fit the model
    model.fit(X_train, y_train)

    # predict the values
    y_pred = model.predict(X_test)

    Rmse, R2, Mae = ModelRgsevaluate(y_pred, y_test)

    return Rmse, R2, Mae, y_pred


# 支持向量机回归
def Svregression(X_train, X_test, y_train, y_test):

    model = SVR(C=2, gamma=1e-07, kernel='linear')
    model.fit(X_train, y_train)

    # predict the values
    y_pred = model.predict(X_test)
    Rmse, R2, Mae = ModelRgsevaluate(y_pred, y_test)

    return Rmse, R2, Mae, y_pred


# 极限学习机
def ELM(X_train, X_test, y_train, y_test):

    model = hpelm.ELM(X_train.shape[1], 1)
    model.add_neurons(20, 'sigm')


    model.train(X_train, y_train, 'r')
    y_pred = model.predict(X_test)


    Rmse, R2, Mae = ModelRgsevaluate(y_pred, y_test)

    return Rmse, R2, Mae, y_pred


# 多元线性回归
def MLR(X_train, X_test, y_train, y_test):
    # 建模
    model = LinearRegression()
    model.fit(X_train, y_train)
    # 预测
    y_pred = model.predict(X_test)
    y_train_pre = model.predict(X_train)
    Rmse, R2, Mae = ModelRgsevaluate(y_pred, y_test)

    return Rmse, R2, Mae, y_pred, y_train_pre

