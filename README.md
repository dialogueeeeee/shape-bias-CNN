# shape-bias-CNN
一种跨域形状偏好 CNN 设计与实现。

## 基于基础形状数据集的分类任务
基础形状分类任务，目的是使网络认识形状，提取形状特征。具体实现都在 ``shape-classification`` 文件夹下。
### 基础形状数据集
这里是形状数据集的生成过程，主要包括以下内容。
- 用于在 224*224 大小的偏黑或偏白（各占 50%）背景中随机生成不同颜色、不同大小、不同位置的形状；
- 使用风格迁移对生成形状进行随机风格化；
- 两者结合成为最终的形状数据集。（注：本次实验用数据集暂未开源。）

#### 随机形状生成 `ShapeGen.py`
- 目录下的 `xxx-ShapeGen.py` 文件用于生成随机颜色、随机大小、随机位置的形状，称之为 **原始形状数据集 OSD (original shape dataset)** ；
- 生成图片大小为 224*224 ；
- 生成图片背景为偏黑或偏白（各占 50% ，该值可根据需要调节，此处设置 50% 是为了使得样本均匀），目的是为了让生成的形状和背景相区分开，避免由于形状颜色和背景颜色相似或相同导致无法识别形状；
- 一代形状数据集包含随机生成的四种形状：**矩形、圆形、椭圆形、三角形** ；
- 二代形状数据集包含随机生成的十种形状：**矩形、圆形、椭圆形、三角形、棱形、五角星形、五边形、六边形、八边形、梯形** ；
- 生成结果示例图：

![example_org](https://user-images.githubusercontent.com/59753705/154614410-5a2b99ff-d736-4a31-944b-56f850b62bef.PNG)

#### 风格化形状图片
- 由原始形状数据集 OSD 生成 **风格化形状数据集 SSD (stylized shape dataset)** ；
- 风格化代码来源于 aaa
- 按照自己要求修改参数，输入命令进行风格化操作，示例命令如下：
``` SHELL
python stylize.py --content-dir F:\pyprj_testfile\shape\rectangle --style-dir F:\graduation_prj\texture-vs-shape_ArticalRec\train --output-dir F:\pyprj_testfile\shape\style_rectangle --num-styles 10 --alpha 0.3 --content-size 0 --style-size 256
```
- 生成结果示例图：

![example_style](https://user-images.githubusercontent.com/59753705/154614451-108bb5ef-1b57-4aae-940e-9cd68abacfb0.PNG)

#### 形状数据集
将原始形状数据集 OSD 和风格化形状数据集 SSD 相结合，即把对应相同形状类放在同一个文件夹下，得到 **形状数据集 SD (shape dataset)** 。

#### 数据集大小
- 一代形状数据集：4类，每类 550 张（原始形状 50 张，风格化形状 500 张），共 2200 张；
- 二代形状数据集：10类，共 12884 张，每类约 1300 张（对于部分类别生成质量不高的图片进行了清除和筛选）。

### 训练结果
结果展示。

## 基于组合复杂形状数据集的分类任务
组合复杂形状分类任务，目的是通过学习复杂形状可以由简单形状组合得到，加深网络对形状的理解。具体实现都在 ``complicated-shape-classification`` 文件夹下。
### 组合复杂形状数据集
- 通过 `complicated-shape-generation.py` 文件生成复杂形状；
- 本项目中，复杂形状定义是由多种简单形状组合生成。具体来说，通过**矩形、圆形、椭圆、三角形**四种简单形状任意组合，共 15 种组合方式，分别生成不同颜色的任意形状；
- 本项目中，第一版本复杂形状最终生成 **15** 个类，每类 **460** 张，共 **6900** 张复杂形状数据集的图像。第一个版本中同一张图片中，形状的线宽和颜色都相同，主要考虑不想让网络通过颜色和线宽的“捷径”来区分形状，而是通过形状的内在特征。示例如下（示例分别为矩形三角形组合，圆形椭圆形组合）。

![image](https://user-images.githubusercontent.com/59753705/157893057-3fe40c25-7640-48cf-901b-5db6c07ddb6d.png)
![image](https://user-images.githubusercontent.com/59753705/157893309-77dc9482-2838-4d6a-898e-5b79ab02628e.png)

- 第二版本复杂形状增加了不同颜色、不同线宽的形状，每类增加 **240** 张，共 **700** 张图片。然后每张图像生成一张风格化图像，每类生成 **700** 张风格化图像。综上所述，第二个版本复杂形状最终生成 **15** 个类，每类 **1400** 张，共 **21000** 张图片。新增图像示例如下。

![image](https://user-images.githubusercontent.com/59753705/158727143-62aa5d09-592a-4bc8-85c8-3790bc944429.png)
![image](https://user-images.githubusercontent.com/59753705/158727068-95a6adb0-2e56-4426-bab6-19b239611ce7.png)

### 训练结果
结果展示。

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
