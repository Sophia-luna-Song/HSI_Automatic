import matplotlib.pyplot as plt
import numpy as np

# 创建一个网格搜索的示例数据
param_grid = {'param1': np.linspace(1, 5, 5), 'param2': np.linspace(1, 3, 3)}
scores = np.random.rand(5, 3)

# 绘制网格搜索的原理图
plt.figure(figsize=(8, 6))
for i, p1 in enumerate(param_grid['param1']):
    for j, p2 in enumerate(param_grid['param2']):
        plt.text(p1, p2, f'Score: {scores[i, j]:.2f}', ha='center', va='center')

plt.xlabel('Param1')
plt.ylabel('Param2')
plt.title('Grid Search Visualization')
plt.grid(True)
plt.show()