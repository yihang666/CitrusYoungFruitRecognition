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


myyolo = yolo.YOLO()
img = cv2.imread("./test6.jpg")
img2 = cv2.imread("./test5.jpg")
image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
image2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
image = Image.fromarray(image)
image2 = Image.fromarray(image2)

res= myyolo.detect_image(image)

box_num = res[1]
res = res[0]
#K.clear_session()
res2 = myyolo.detect_image(image2)

res3 = myyolo.detect_image(image)
cv2.imshow("Image", res)
cv2.waitKey()