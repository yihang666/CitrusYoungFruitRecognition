import cv2
import os
def cutimage(dir,suffix):
  for root,dirs,files in os.walk(dir):
    for file in files:
      filepath = os.path.join(root, file)
      filesuffix = os.path.splitext(filepath)[1][1:]
      if  filesuffix in suffix:    #遍历找到指定后缀的文件名["jpg",png]等
        image = cv2.imread(file)  #opencv剪切图片   
        #cv2.imshow(file,image) 
        dim =(242,200)           #指定尺寸w*h
        resized =cv2.resize(image,dim,interpolation = cv2.INTER_AREA)  #这里采用的插值法是INTER_LINEAR
        #cv2.imshow("resize:%s"%file,resized)
        cv2.imwrite("../cv/%s"%file,resized)  #保存文件  
  cv2.waitKey(0)         #退出
 
suffix = ["jpg"]
dir = '.'
cutimage(dir,suffix)

