from Regression.ClassicRgs import Pls, Svregression, ELM, MLR


def QuantitativeAnalysis(model, X_train, X_test, y_train, y_test, num=30):

    if model == "Pls":
        Rmse, R2, Mae, y_pre = Pls(X_train, X_test, y_train, y_test, num=num)
    elif model == "SVR":
        Rmse, R2, Mae, y_pre = Svregression(X_train, X_test, y_train, y_test)
    elif model == "ELM":
        Rmse, R2, Mae, y_pre = ELM(X_train, X_test, y_train, y_test)
    elif model == "MLR":
        Rmse, R2, Mae, y_pre, y_train_pred = MLR(X_train, X_test, y_train, y_test)
    else:
        print("no this model of QuantitativeAnalysis")

    return Rmse, R2, Mae, y_pre, y_train_pred

