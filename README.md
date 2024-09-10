# HSI_Automatic

该方法在利用玉米种子高光谱图像的单粒油脂含量预测中验证，并取得良好效果。

相关文章发表在《Food Chemistry》期刊，Q1 8.5，欢迎引用。
原文链接：https://www.sciencedirect.com/science/article/abs/pii/S0308814624025822


可见和近红外高光谱成像技术结合人工智能技术已经称为研究热点。其能够获取种子样本中分子的泛音和组合振动信息。但由于这些信号较弱且解析度较低，通常需要借助化学计量学或人工智能方法分析光谱与组分之间的关系。

项目包括了高光谱图像预处理、关键波段选择、数据划分以及回归算法四个处理步骤的算法集，并在四个阶段上利用网格搜索进行参数优化。
另外，还包括数据加载与增强、种子高光谱图像自动分割与ROI提取、光谱与图像可视化以及评估方法。

## 1、图像自动分割
  
  ![image](https://github.com/Sophia-luna-Song/HSI_Automatic/assets/59360539/adba07c5-b5c1-47eb-9227-b9b99b81d7c2)

## 2、光谱与图像可视化
  
  ### 光谱可视化
  
  ![image](https://github.com/Sophia-luna-Song/HSI_Automatic/assets/59360539/27f145cf-924f-4413-b6d5-51064379ad24)

  ### 图像灰度图
  
  ![image](https://github.com/Sophia-luna-Song/HSI_Automatic/assets/59360539/219b97c3-a50e-4b2e-86ae-0e9bf322dcf9)
  
  ### 图像伪彩图
  
  ![image](https://github.com/Sophia-luna-Song/HSI_Automatic/assets/59360539/1fe2eedd-c2f7-45cb-aef8-6319c316ec84)

  

## 总结：
代码现仅供学术使用，若对您的学术研究有帮助，请引用本人的论文（https://www.sciencedirect.com/science/article/abs/pii/S0308814624025822

同时，未经许可不得用于商业化应用，欢迎大家继续补充更多的高光谱图像处理方法。（代码参考了https://github.com/FuSiry/OpenSA）
