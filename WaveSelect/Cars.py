import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import KFold

# ref: https://blog.csdn.net/qq2512446791


def CARS_Cloud(X, y, N=20, f=30, cv=5):
    '''
    X : 光谱矩阵 nxm
    y : 浓度阵（化学值）
    N : 迭代次数
    f : 主成分数量
    cv: 交叉验证数量

    return :
            OptWave: 关键波长
    '''
    p = 0.8
    m, n = X.shape
    u = np.power((n/2), (1/(N-1)))
    k = (1/(N-1)) * np.log(n/2)
    cal_num = int(np.round(m * p))
    b2 = np.arange(n)
    WaveData = []
    RMSECV = []

    for i in range(1, N+1):
        wave_num = int(np.round(u * np.exp(-k * i) * n))
        cal_index = np.random.choice(m, size=cal_num, replace=False)
        wave_index = b2[:wave_num]

        xcal = X[cal_index, :][:, wave_index]
        ycal = y[cal_index]

        # 使用 PLS 进行内部验证
        kf = KFold(n_splits=cv)
        cv_errors = []
        for train_index, test_index in kf.split(xcal):
            pls = PLSRegression(n_components=min(f, wave_num))
            pls.fit(xcal[train_index], ycal[train_index])
            y_pred = pls.predict(xcal[test_index])
            cv_errors.append(np.mean((ycal[test_index] - y_pred.flatten())**2))
        RMSECV.append(np.mean(cv_errors))

        # 保存当前迭代的波长数据
        d = np.zeros(n)
        d[wave_index] = 1
        WaveData.append(d)

    # 选择最优波长
    MinIndex = np.argmin(RMSECV)
    OptWave = np.nonzero(WaveData[MinIndex])[0]

    return OptWave