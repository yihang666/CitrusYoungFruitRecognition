# CitrusYoungFruitRecognition

##最终模型现实效果图
<p align="center">
  <img src="http://www.tlquant.com/wp-content/uploads/2020/05/1.png" width="450" height="300" />
</p>

##原始数据集下载地址：https://drive.google.com/open?id=1z5tWi7K0Yn0gQoPjWTSrZ1aD7GGkR4c2

##训练完成后模型的地址：https://drive.google.com/open?id=140xKM3wFzK-rAlQ8lfK9OZ9sqhavwfLk



##文档内容
- [DataAugmentation](#DataAugmentation)
- [TrainModel](#TrainModel)
- [TestModel](#TestModel)
- [ServerDeployment](#ServerDeployment)
- [AndroidAPPDev](#AndroidAPPDev)

##DataAugmentation

##TrainModel

##TestModel
 首先，我们需要将mAP-master/data中的xml格式标注(VOC 2007)转换成本代码所需txt格式，转换由mAP-master/scripts/extra/convert_keras-yolo3.py完成
（我们在下面提供转换后的数据，直接下载input文件夹中的三个数据即可）
如需mAP-master/data原始格式数据来自行尝试转换，链接如下：

https://drive.google.com/open?id=1sR0qR-X_tc6NLsYmcD24LFKtdJrk6c0O

###input文件夹
其中mAP-master/input/detection-results/ 中的数据压缩包地址如下
https://drive.google.com/open?id=113O5BRupHh-Qd9YZI-Q3ayOzex6RM6KT

mAP-master/input/ground-truth/ 中的数据如下
https://drive.google.com/open?id=1J9eqj2Y2bCTfWHEspAyed5lmzBtUPFVM

mAP-master/input/image-optional/ 中的数据如下
https://drive.google.com/open?id=1OCVC6MvoaBAaGPhQ9eTcUOEvB7BrlTvK

###output文件夹
所有的输出图片压缩包链接如下
https://drive.google.com/open?id=1Vzeqe6vRgTY6NDR4j-qdXKhnh6a-icPW

##ServerDeployment

##AndroidAPPDev
