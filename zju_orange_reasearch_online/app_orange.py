# @Author: Dwivedi Chandan
# @Date:   2019-08-05T13:35:05+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2019-08-07T11:52:45+05:30


# import the necessary packages
import numpy as np
import yolo
import argparse
import time
import cv2
import os
from flask import Flask, request, Response, jsonify
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
    img = request.files["image"].read()
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
    res = myyolo.detect_image(image)
    box_num = res[1]
    res = res[0]
    # image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # show the output image
    #cv2.imshow("Image", res)
    #cv2.waitKey()

    image = cv2.cvtColor(np.array(res), cv2.COLOR_RGB2BGR)
    #image=cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
    np_img=Image.fromarray(image)
    img_encoded=image_to_byte_array(np_img)
    dict1 = {"index": "haha"}
    resp = Response(response=img_encoded, status=200, mimetype="image/jpeg")
    return Response(response=img_encoded, status=200, mimetype="image/jpeg")



    # start flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=3389)
    #app.run(debug=True)