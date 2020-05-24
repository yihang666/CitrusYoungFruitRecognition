# @Author: Dwivedi Chandan
# @Date:   2019-08-05T13:35:05+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2019-08-07T11:52:45+05:30


# import the necessary packages
import numpy as np
from werkzeug.utils import secure_filename

import yolo
import argparse
import time
import cv2
import os
from flask import Flask, request, Response, jsonify, render_template
import jsonpickle
#import binascii
import io as StringIO
import base64
from io import BytesIO
import io
import json
from PIL import Image
from keras import backend as K

# construct the argument parse and parse the arguments

confthres = 0.3
nmsthres = 0.1
yolo_path = './'



def image_to_byte_array(image:Image):
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format='PNG')
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr

labelsPath="yolo_v3/coco_orange.names"
cfgpath="yolo_v3/yolov3_orange.cfg"
wpath="yolo_v3/yolov3_orange.weights"
# Initialize the Flask application
i = 1
app = Flask(__name__)

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def main():
    # load our input image and grab its spatial dimensions
    #image = cv2.imread("./test1.jpg")
    img0 = request.files["image"]
    img = img0.read()
    img = Image.open(io.BytesIO(img))
    npimg=np.array(img)
    image=npimg.copy()
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    global i
    global myyolo
    if(i==1):
        myyolo = yolo.YOLO()
        res = myyolo.detect_image(image)
        i=0
    else:
        res = myyolo.detect_image(image)
    box_num = res[1]
    imageSplit = res[2]
    res = res[0]

    if imageSplit==1:
        pass
    else:
        target = Image.new('RGB',(res.width,res.height))
        box_num = 0
        for row in range(2):
            for col in range(2):
                try:
                    w = image.width / 2
                    h = image.height / 2
                    cropBox = (col * w, row * h, w * (col + 1), h * (row + 1))
                    temp = image.crop(cropBox)
                    resTemp = myyolo.detect_image(temp)
                    a = int(w * col)  # 图片距离左边的大小
                    b = int(h * row)  # 图片距离上边的大小
                    c = int(w * (col + 1))  # 图片距离左边的大小 + 图片自身宽度
                    d = int(h * (row + 1))  # 图片距离上边的大小 + 图片自身高度
                    box_num = box_num + resTemp[1]
                    imgSplitTemp = resTemp[0]
                    target.paste(imgSplitTemp, (a, b, c, d))
                except:
                    pass
        res=target
    # image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # show the output image
    #cv2.imshow("Image", res)
    #cv2.waitKey()

    image = cv2.cvtColor(np.array(res), cv2.COLOR_RGB2BGR)
    image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    np_img=Image.fromarray(image)
    img_encoded=image_to_byte_array(np_img)

    basepath = os.path.dirname(__file__)
    filename =  secure_filename(img0.filename)
    upload_path = os.path.join(basepath, 'static/images', filename)
    np_img.save(upload_path)

    back_url = ('http://47.97.105.170:8000/'+filename)

    img_stream_bgr = base64.b64encode(image)
    img_stream_rgb = base64.b64encode(image_rgb)
    img_stream_rgb_str = img_stream_rgb.decode('ascii')


    dict1 = {"flie_name":filename,
             "box_num": box_num,
             "img_encoded" :0,
             "img_strean(base64)":0,
             "back_url":back_url}


    #  "img_encoded" :str(img_encoded),
    #"img_strean(base64)":str(img_stream_rgb)

    return jsonify(dict1)



    # start flask app
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0', port=3389)
    #app.run(debug=True)