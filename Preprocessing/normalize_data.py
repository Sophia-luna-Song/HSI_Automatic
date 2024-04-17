import numpy as np


# 归一化
def normalize_data(data):
    # 计算每个特征的最小值和最大值
    data = np.array(data)  # 将数据转换为NumPy数组
    min_vals = np.min(data, axis=1, keepdims=True)
    max_vals = np.max(data, axis=1, keepdims=True)

    # 处理最小值和最大值均为0的情况
    # 处理最小值为零的情况
    # for i in range(len(data)):
    # 对每个特征进行归一化
    normalized_data = (data - min_vals) / (max_vals - min_vals)

    return normalized_data


# # 假设data是一个形状为(n, 256)的NumPy数组，表示包含n个样本的数据集
# normalized_data = normalize_data(data)