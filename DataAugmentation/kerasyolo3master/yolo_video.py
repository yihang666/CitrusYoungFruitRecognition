import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import os
import matplotlib.pyplot as plt
"""
def detect_img(yolo):
    while True:
        img = input('E:/ZJUCVresearch/VOCdevkit/VOC2007/JPEGImages/IMG_4027.jpg')
        #outdir = "E:/ZJUCVresearch/VOCdevkit/VOC2007/SegmentationClass"
        try:
            image = Image.open(img)
            plt.figure("orange")
            plt.imshow(image)
            plt.show()
            print(2)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            print(1)
            r_image.show()
            plt.figure("orange")
            plt.imshow(r_image)
            plt.show()
        
    yolo.close_session()
"""
import glob
import cv2

def detect_img(yolo):
    path = "D:\ZJUCVresearch\kerasyolo3master\VOCdevkit\VOC2007\JPEGImages\*.jpg"
    outdir = "D:\ZJUCVresearch\kerasyolo3master\VOCdevkit\VOC2007\SegmentationClass"
   
    for jpgfile in glob.glob(path):
        img = Image.open(jpgfile)
        img = yolo.detect_image(img)
        img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    yolo.close_session()



FLAGS = None



if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    
    #Command line options
    
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=True, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    
    #Command line positional arguments -- for video detection mode
    
    
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='D:/ZJUCVresearch/VOCdevkit/VOC2007/JPEGImages/5.jpg',
        help = "Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="D:/ZJUCVresearch/kerasyolo3master/VOCdevkit/VOC2007/SegmentationObject",
        help = "[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        #Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
        #print(1)
    elif "input" in FLAGS:
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)

    else:
        print("Must specify at least video_input_path.  See usage with --help.")
