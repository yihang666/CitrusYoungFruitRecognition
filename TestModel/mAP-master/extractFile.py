# -*- coding: utf-8 -*-
#  根据图片链接列表获取图片保存到本地
import shutil
import urllib
from urllib.request import urlretrieve
import os
# 解决
import ssl


def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exit!" % (srcfile))
    else:
        fpath,fname=os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile,dstfile)
        #print("copy %s" % (srcfile,dstfile))

'''
通过txt网址文件，现在图片到本地
'''
def download_image():
    path = 'D:/ZJUCVresearch/keras-yolo3-master-soccer/model_data/2007_test.txt'
    categories = ['ladder']
    for category in categories:
        # 新建存储ladder文件夹存储图片
        os.makedirs('data/%s' % category, exist_ok=True)
        # 读取txt文件
        with open(path) as file:
            urls = file.readlines()
            line = []
            for i in range(len(urls)):
                line.append((urls[i].split())[0])
            urls = line
            # 计算链接地址条数
            n_urls = len(urls)
            # 遍历链接地址下载图片
            for i, url in enumerate(urls):
                try:
                     # 请求下载图片，并截取最后链接第一最后一节字段命名图片
                     shutil.copy(url, 'D:/ZJUCVresearch/mAP-master/data/ladder')
                     #urllib.request.urlretrieve(url, 'data/%s/%s' % (category, url.strip().split('/')[-1]))
                     print('%s %i/%i' % (category, i, n_urls))
                except:
                     print('%s %i/%i' % (category, i, n_urls), 'no image')

def download_annotation():
    path = 'D:/ZJUCVresearch/keras-yolo3-master-soccer/model_data/2007_test.txt'
    annotation_path = 'D:/ZJUCVresearch/keras-yolo3-master-soccer/VOCdevkit/VOC2007/Annotations/'
    categories = ['annotation']
    for category in categories:
        # 新建存储ladder文件夹存储图片
        os.makedirs('data/%s' % category, exist_ok=True)
        # 读取txt文件
        with open(path) as file:
            urls = file.readlines()
            line = []
            for i in range(len(urls)):
                urls[i]=urls[i].replace('.jpg','.xml')
                urls[i]=urls[i].strip().split('/')[-1]
                a = [annotation_path,urls[i]]
                urls[i]=''.join(a)
                line.append((urls[i].split())[0])

            urls = line
            # 计算链接地址条数
            n_urls = len(urls)
            # 遍历链接地址下载图片
            for i, url in enumerate(urls):
                try:
                     # 请求下载图片，并截取最后链接第一最后一节字段命名图片
                     shutil.copy(url, 'D:/ZJUCVresearch/mAP-master/data/annotation')
                     #urllib.request.urlretrieve(url, 'data/%s/%s' % (category, url.strip().split('/')[-1]))
                     print('%s %i/%i' % (category, i, n_urls))
                except:
                     print('%s %i/%i' % (category, i, n_urls), 'no image')

if __name__ == '__main__':
    download_annotation();