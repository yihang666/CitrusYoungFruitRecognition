# CitrusYoungFruitRecognition

## 最终模型现实效果图
<p align="center">
  <img src="http://www.tlquant.com/wp-content/uploads/2020/05/1.png" width="450" height="300" />
</p>


## 原始数据集下载地址：
https://drive.google.com/open?id=1z5tWi7K0Yn0gQoPjWTSrZ1aD7GGkR4c2

## 训练完成后模型的地址：
https://drive.google.com/open?id=140xKM3wFzK-rAlQ8lfK9OZ9sqhavwfLk



## 文档内容
- [DataAugmentation数据增强](#DataAugmentation)
- [TrainModel模型训练](#TrainModel)
- [TestModel模型性能检测](#TestModel)
- [ServerDeployment服务器部署](#ServerDeployment)
- [AndroidAPPDev安卓端应用开发](#AndroidAPPDev)
- [备注](#AndroidAPPDev)


## DataAugmentation数据增强

rename.bat为批处理文件名工具，快速把文件名改为数字序列（1，2，3，4.........）

数据增强调用 zju_orange_research目录下data_augmentation.py

增强后数据存储于zju_orange_research/VOCdevkit/VOC2007文件夹
下载训练用数据集也存放在该目录下

增强后标签链接：https://drive.google.com/open?id=1MqXM2WxCj5EYGiRo4IKwD2zc7cEGL71L

增强后图片数据集链接：https://drive.google.com/open?id=1YIJSKqzqndr7K5jkev7ojygL1JJOsPG-

## TrainModel模型训练


YOLOv3的网络架构详情见zju_orange_research/yolov3.cfg配置文件

训练模型请参考zju_orange_research目录下readme，使用train.py(是否进行迁移学习请自选)，训练时超参数的设置也在train.py文件中

默认的训练为迁移学习原模型50epoch，再解开所有隐藏层训练50epoch，解开所有隐藏层时请注意显卡的显存是否溢出，及时减小batch_size


## TestModel模型性能检测
 首先，我们需要将mAP-master/data中的xml格式标注(VOC 2007)转换成本代码所需txt格式，转换由mAP-master/scripts/extra/convert_keras-yolo3.py完成
（我们在下面提供转换后的数据，直接下载input文件夹中的三个数据即可）
如需mAP-master/data原始格式数据来自行尝试转换，链接如下：

https://drive.google.com/open?id=1sR0qR-X_tc6NLsYmcD24LFKtdJrk6c0O

### input文件夹
其中mAP-master/input/detection-results/ 中的数据压缩包地址如下
https://drive.google.com/open?id=113O5BRupHh-Qd9YZI-Q3ayOzex6RM6KT

mAP-master/input/ground-truth/ 中的数据如下
https://drive.google.com/open?id=1J9eqj2Y2bCTfWHEspAyed5lmzBtUPFVM

mAP-master/input/image-optional/ 中的数据如下
https://drive.google.com/open?id=1OCVC6MvoaBAaGPhQ9eTcUOEvB7BrlTvK

### output文件夹
所有的输出图片压缩包链接如下
https://drive.google.com/open?id=1Vzeqe6vRgTY6NDR4j-qdXKhnh6a-icPW

## ServerDeployment服务器部署

推荐使用bt面板将，将zju_orange_reasearch_online部署于云服务器上

服务器上不间断运行app_orangejson.py即可

## AndroidAPPDev
安卓APP源代码地址见
https://github.com/yihang666/orange_detection_android

安卓应用程序直接下载地址见
http://www.tlquant.com/index.php/2020/05/07/%e6%9f%91%e6%a9%98%e5%b9%bc%e6%9e%9c%e8%af%86%e5%88%abapp%e4%b8%8b%e8%bd%bd%e9%93%be%e6%8e%a5/

## 备注
环境搭建时注意不要使用tensorflow2

## Author:
* **Yihang Zhu**

