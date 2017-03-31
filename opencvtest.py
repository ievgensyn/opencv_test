#!/usr/bin/env python

import numpy as np
import cv2
import datetime
import time

"""
   
   there is two methods using here: BackgroundSubtractorKNN() + MOG2()
"""


def motion_detection(cap):

    cap = cv2.VideoCapture(0)  #get the video from any valid camera

    fgbg = cv2.createBackgroundSubtractorKNN()
    fgbg2 = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)
        fgbgmask2 = fgbg2.apply(frame)

        cv2.putText(frame, datetime.datetime.now().strftime("%Y-%m-%d, %A || %H:%M:%S"), (8, 470),\
        cv2.FONT_HERSHEY_DUPLEX, 0.75, (10, 215, 0))

        cv2.imshow('frame_2', fgmask)
        cv2.imshow('frame', frame)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
