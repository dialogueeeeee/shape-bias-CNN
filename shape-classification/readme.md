## 概述
这是形状检测器的实现。主要通过构造形状数据集，对卷积神经网络进行训练，达到形状分类器的效果。

### 数据集摆放 `/dataset` 文件夹
- 将训练数据放置在 `dataset/train/` 文件夹下，按照分类放置图片，即对应类别图片放置在对应类别文件夹下；
- 将验证数据放置在 `dataset/val/` 文件夹下，按照分类放置图片。

### 生成数据集 `.txt` 文件
- 运行 `txt_annotation.py` 得到根目录下的 `cls_train.txt` 和 `cls_test.txt` 文件，分别指向对应的训练和验证数据集的图片位置；

### 训练模型
- 按照自己需求配置 `train.py` 文件，本次实验配置如下：
```
backbone        = "resnet50"
lr              = 1e-4
Batch_size      = 16
Freeze_Epoch    = 50
Epoch           = 200

epoch_step      = num_train // Batch_size
epoch_step_val  = num_val // Batch_size
```
- 运行 `train.py` 文件，开始训练，得到权值文件(.pth) 。

### 使用训练好的模型进行预测
- 从权值文件中选择 loss 较小的文件进行预测，本项目选取 `ep181-loss0.011-val_loss0.014.pth` 文件；
- 修改并运行 `predict.py` 文件，使用训练好的模型进行预测；
- 预测结果良好，准确率较高，预测示例如下：
- 当输入图像为形状较为明显的自然图像时，也能准确预测形状，预测示例如下：在一定程度上说明该网络能提取物体的形状特征，有待进一步研究。
