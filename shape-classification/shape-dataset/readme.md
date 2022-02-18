## 概述
这里是形状数据集的生成过程，主要包括以下内容。
- 用于在 224*224 大小的偏黑或偏白（各占 50%）背景中随机生成不同颜色、不同大小、不同位置的形状；
- 使用风格迁移对生成形状进行随机风格化；
- 两者结合成为最终的形状数据集。（注：本次实验用数据集暂未开源。）

### 随机形状生成 `ShapeGen.py`
- 目录下的 `xxx-ShapeGen.py` 文件用于生成随机颜色、随机大小、随机位置的形状，称之为 **原始形状数据集 OSD (original shape dataset)** ；
- 生成图片大小为 224*224 ；
- 生成图片背景为偏黑或偏白（各占 50% ，该值可根据需要调节，此处设置 50% 是为了使得样本均匀），目的是为了让生成的形状和背景相区分开，避免由于形状颜色和背景颜色相似或相同导致无法识别形状；
- 目前可以随机生成四种形状：**矩形、圆形、椭圆形、三角形** ；
- 生成结果示例图：
![example_org](https://user-images.githubusercontent.com/59753705/154614410-5a2b99ff-d736-4a31-944b-56f850b62bef.PNG)


### 风格化形状图片
- 由原始形状数据集 OSD 生成 **风格化形状数据集 SSD (stylized shape dataset)** ；
- 风格化代码来源于 aaa
- 按照自己要求修改参数，输入命令进行风格化操作，示例命令如下：
``` SHELL
python stylize.py --content-dir F:\pyprj_testfile\shape\rectangle --style-dir F:\graduation_prj\texture-vs-shape_ArticalRec\train --output-dir F:\pyprj_testfile\shape\style_rectangle --num-styles 10 --alpha 0.3 --content-size 0 --style-size 256
```
- 生成结果示例图：
- 

### 形状数据集
将原始形状数据集 OSD 和风格化形状数据集 SSD 相结合，即把对应相同形状类放在同一个文件夹下，得到 **形状数据集 SD (shape dataset)** 。
