# shape-bias-CNN
一种跨域形状偏好 CNN 设计与实现
## 基于双任务的形状理解网络
- 本项目通过同时训练两个形状相关任务，希望网络加强对形状的理解，并在迁移学习中获得形状偏好；
- 任务一：基于基础形状数据集的（10 类）分类任务，任务 1 详情可见文件夹 ``shape-classification``；
- 任务二：基于组合复杂形状数据集的（15 类）分类任务，任务 2 详情可见文件夹 ``complicated-shape-classification``；
- 联合损失函数：**L_total = L1 + α * L2** ，其中 α 为可调超参数。
- 以下是基于双任务的形状理解网络训练原理示意图。
![双任务预训练结构02](https://user-images.githubusercontent.com/59753705/158997620-26a9f09e-a258-418a-b75a-71eaac26350a.png)

## 基于形状理解网络的迁移学习研究
基于形状理解网络的迁移学习研究
### 迁移学习形状偏好研究 (shape-bias) 
- salience maps
- Saturation
- patch-shuffle
### 迁移学习跨域分类任务
PACS dataset
### 迁移学习小样本分类任务
few-shot classification
