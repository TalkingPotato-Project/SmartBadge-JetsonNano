import jetson.inference
import jetson.utils

import numpy as np
from playsound import playsound
import os

import time
import board
import busio
import adafruit_adxl34x

import requests
import json


class segmentationBuffers:


    def __init__(self, net, args):
        self.net = net
        self.mask = None
        self.overlay = None
        self.composite = None
        self.class_mask = None
        
        self.use_stats = args.stats
        self.use_mask = "mask" in args.visualize
        self.use_overlay = "overlay" in args.visualize
        self.use_composite = self.use_mask and self.use_overlay
        
        if not self.use_overlay and not self.use_mask:
            raise Exception("invalid visualize flags - valid values are 'overlay' 'mask' 'overlay,mask'")
             
        self.grid_width = 5
        self.grid_height = 5
        self.num_classes = net.GetNumClasses()
        
        self.area_count = 0
        self.area_num = 0
        self.area_notcount = 0
        self.area_notnum = 0

        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.accelerometer = adafruit_adxl34x.ADXL345(self.i2c)
        self.accelerometer.enable_motion_detection(threshold=25)
        self.walkCount = 0
        self.walkFlag = True
        
        self.URL = 'http://112.158.50.42:9080/jaywalking/1234567890/'
        self.headers = {'Content-Type': 'application/json', 'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
        self.data = {"smartBadgeID:1234567890"}

    @property
    def output(self):
        if self.use_overlay and self.use_mask:
            return self.composite
        elif self.use_overlay:
            return self.overlay
        elif self.use_mask:
            return self.mask
            
    def Alloc(self, shape, format):
        if self.overlay is not None and self.overlay.height == shape[0] and self.overlay.width == shape[1]:
            return

        if self.use_overlay:
            self.overlay = jetson.utils.cudaAllocMapped(width=shape[1], height=shape[0], format=format)

        if self.use_mask:
            mask_downsample = 2 if self.use_overlay else 1
            self.mask = jetson.utils.cudaAllocMapped(width=shape[1]/mask_downsample, height=shape[0]/mask_downsample, format=format) 

        if self.use_composite:
            self.composite = jetson.utils.cudaAllocMapped(width=self.overlay.width+self.mask.width, height=self.overlay.height, format=format) 

        if self.use_stats:
            self.class_mask = jetson.utils.cudaAllocMapped(width=self.grid_width, height=self.grid_height, format="gray8")
            self.class_mask_np = jetson.utils.cudaToNumpy(self.class_mask)
            
    def ComputeStats(self):
        if not self.use_stats:
            return
            
        self.net.Mask(self.class_mask, self.grid_width, self.grid_height)

        class_histogram, _ = np.histogram(self.class_mask_np, self.num_classes)

        area_width_first = int(self.grid_width*(0.4))
        area_width_last = int(self.grid_width*(0.6))
        area_height_first = int(self.grid_height*(0.8))
        area_height_last = int(self.grid_height)

        myclass = self.class_mask_np
        my_area = myclass[area_height_first:area_height_last, area_width_first:area_width_last]

        self.area_notnum = my_area[0][0][0]

        if self.area_num != self.area_notnum:
            if self.area_count == 3 :
                self.area_num = self.area_notnum
                self.area_count = 0

                if self.area_num == 1 : #도로일 때
                    os.system("gst-play-1.0 " + "--volume=2 "  + "audio/roadway.mp3")
                elif self.area_num == 3 : #횡단보도 앞일 때
                    os.system("gst-play-1.0 " + "--volume=2 " + "audio/crosswalk.mp3")
            else:
                self.area_count = self.area_count + 1
        else:
            self.area_count = 0

        if self.area_num == 1:
            if self.accelerometer.events.get("motion"):
                self.walkCount = self.walkCount + 1
            if self.walkCount > 1 and self.walkFlag:
                self.walkFlag = False
                os.system("gst-play-1.0 " + "--volume=2 " + "audio/jaywalking.mp3")
                try:
                    print("Complete send jaywalking to server...")
                    requests.post(self.URL, headers=self.headers)
                except:
                    print("Network connect failed...")
            print("WalkCount : ", self.walkCount)
        else:
            self.walkCount = 0
            self.walkFlag = True
