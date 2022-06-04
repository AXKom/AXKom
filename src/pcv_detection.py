#!/usr/bin/env python

import numpy as np
import argparse
from plantcv import plantcv as pcv
import cv2
from src.detectedFrame import DetectedFrame
from src.annotation import Annotation


def detect(img,plantName):

    if np.average(img) < 50:
        pcv.fatal_error("Night Image")
    else:
        pass

    # STEP 2: Normalize the white color so you can later
    # compare color between images.
    # Inputs:
    #   img = image object, RGB colorspace
    #   roi = region for white reference, if none uses the whole image,
    #         otherwise (x position, y position, box width, box height)

    # white balance image based on white toughspot

    img1 = img

   

    # STEP 5: Convert image from RGB colorspace to LAB colorspace
    # Keep only the green-magenta channel (grayscale)
    # Inputs:
    #    img     = image object, RGB colorspace
    #    channel = color subchannel ('l' = lightness, 'a' = green-magenta , 'b' = blue-yellow)

    a = pcv.rgb2gray_lab(rgb_img=img1, channel='a')

    # STEP 6: Set a binary threshold on the saturation channel image
    # Inputs:
    #    img         = img object, grayscale
    #    threshold   = threshold value (0-255)
    #    max_value   = value to apply above threshold (usually 255 = white)
    #    object_type = light or dark
    #       - If object is light then standard thresholding is done
    #       - If object is dark then inverse thresholding is done

    img_binary = pcv.threshold.binary(gray_img=a, threshold=120, max_value=255, object_type='dark')
    #                                                   ^
    #                                                   |
    #                                     adjust this value
    # STEP 7: Fill in small objects (speckles)
    # Inputs:
    #    bin_img  = image object, binary. img will be returned after filling
    #    size = minimum object area size in pixels (integer)

    fill_image = pcv.fill(bin_img=img_binary, size=100)
    #                                          ^
    #                                          |
    #                           adjust this value
    # STEP 8: Dilate so that you don't lose leaves (just in case)
    # Inputs:
    #    img    = input image
    #    ksize  = kernel size
    #    i      = iterations, i.e. number of consecutive filtering passes

    dilated = pcv.dilate(gray_img=fill_image, ksize=2, i=1)
    # STEP 9: Find objects (contours: black-white boundaries)
    # Inputs:
    #    img  = image that the objects will be overlayed
    #    mask = what is used for object detection
    _annotations=[] 
    if len(np.shape(img)) == 2:
        ori_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    objects, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2:]
    for i, obj in enumerate(objects):
        height, width = np.shape(img)[:2]
        x, y, w, h = cv2.boundingRect(obj)
        if w>100 and h>100:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
            _annotations.append(Annotation(plantName,x,y,(x+w),(y+h)))

    return DetectedFrame(dilated,img,_annotations)
        
