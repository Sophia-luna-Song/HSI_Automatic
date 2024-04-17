import pandas as pd

# 读取Excel文件
df = pd.read_excel('F:/game/小论文/paper3/数据/结果数据/绘图3D曲面.xlsx')

# 使用pivot函数重构DataFrame，关键波长个数为列号，窗口大小为行号，R2为填充值
pivoted_df = df.pivot(index='Window Size', columns='key band count', values='R2')

# 显示重构后的DataFrame
pivoted_df


