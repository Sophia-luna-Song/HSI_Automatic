
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import pandas as pd


# 计算均方误差，R2，平均绝对误差
def ModelRgsevaluate(y_pred, y_true):

    mse = mean_squared_error(y_true, y_pred)
    R2  = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)

    return np.sqrt(mse), R2, mae


# 计算均方根误差，R2，平均绝对误差
def ModelRgsevaluatePro(y_pred, y_true, yscale):

    yscaler = yscale
    y_true = yscaler.inverse_transform(y_true)
    y_pred = yscaler.inverse_transform(y_pred)

    mse = mean_squared_error(y_true, y_pred)
    R2  = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)

    return np.sqrt(mse), R2, mae


# 计算
def ModelRgsEvaluatePlot(X, y):
    X = X.reshape(-1, 1)
    reg = LinearRegression().fit(X, y)
    coef = round(reg.coef_[0][0], 4)
    intercept = round(reg.intercept_[0], 3)
    model = str('y=') + str(coef) + 'x+' + str(intercept)
    X = X.reshape(-1, 1)
    y_predict = reg.predict(X)
    delta = abs(y - y_predict)
    data = pd.Series(delta.reshape(1, -1)[0])
    index = data[data < 4].index
    return index, model, coef, intercept, y_predict