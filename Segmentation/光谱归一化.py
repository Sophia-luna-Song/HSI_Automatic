import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


# 最大最小归一化
def MinMaxTrans(data, file_path):
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    # 将归一化后的数据转换回 DataFrame
    normalized_df = pd.DataFrame(normalized_data)

    # 载入第一行（波段序号）
    band_numbers = pd.read_excel(file_path, header=None, nrows=1)

    # 将波段序号添加到归一化数据的顶部
    final_df = pd.concat([band_numbers, normalized_df], ignore_index=True)

    return final_df


# 标准归一化
def StandardTrans(data, file_path):
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data)

    normalized_df = pd.DataFrame(normalized_data)
    band_numbers = pd.read_excel(file_path, header=None, nrows=1)

    final_df = pd.concat([band_numbers, normalized_df], ignore_index=True)

    return final_df


# 光谱最大值归一化
def MaxTrans(data, file_path):
    normalized_data = data/4096

    normalized_df = pd.DataFrame(normalized_data)
    band_numbers = pd.read_excel(file_path, header=None, nrows=1)

    final_df = pd.concat([band_numbers, normalized_df], ignore_index=True)

    return final_df


def main():
    # 载入数据（跳过第一行，因为它包含波段序号）
    file_path = 'F:\game\小论文\paper3\数据\\15品种\玉米288传统方法获取平均光谱.xlsx'  # 请替换为您的文件路径
    df = pd.read_excel(file_path, header=None, skiprows=1)
    data = df.iloc[:, :].values

    final_df = MinMaxTrans(data, file_path)
    # 将归一化的数据保存到新的 Excel 文件
    output_file_path = 'F:\game\小论文\paper3\数据\\15品种\玉米288种子MaxMin归一化光谱数据.xlsx'  # 您可以指定所需的输出文件路径
    final_df.to_excel(output_file_path, index=False, header=False)


if __name__ == '__main__':
    main()
