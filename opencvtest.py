#!/usr/bin/env python

import numpy as np
import cv2
import datetime
import time
import argparse
import sys

"""
Data matrix detector sample.
Usage:
   video_dmtx {<video device number>|<video file name>}

   Generate a datamatrix from  from http://datamatrix.kaywa.com/ and print it out.
   NOTE: This only handles data matrices, generated for text strings of max 3 characters

   Resize the screen to be large enough for your camera to see, and it should find an read it.

Keyboard shortcuts:

   q or ESC - exit
   space - save current image as datamatrix<frame_number>.jpg
"""


def motion_detection(cap):

    cap = cv2.VideoCapture(0)  #get the video from any valid camera

    fgbg = cv2.BackgroundSubtractorMOG()

    while True:
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)

        cv2.putText(frame, datetime.datetime.now().strftime("%Y-%m-%d, %A || %H:%M:%S"), (8, 470),\
        cv2.FONT_HERSHEY_DUPLEX, 0.75, (10, 215, 0))

        cv2.imshow('frame_2', fgmask)
        cv2.imshow('frame', frame)

        k = 0xFF & cv2.waitKey(10)

        if k == 27:
            cv2.destroyAllWindows()
        break
