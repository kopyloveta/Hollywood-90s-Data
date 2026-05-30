#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 27.01.2019 13:44:53 MSK

import cv2

pth = '/home/boris/Видео/AK/film/Anna.Karenina.1997.TRIPLE.BDRip.XviD.AC3.-HQCLUB/Anna.Karenina.1997.TRIPLE.BDRip.XviD.AC3.-HQCLUB.avi'

def main():
    vidcap = cv2.VideoCapture(pth)
    success,image = vidcap.read()
    count = 0
    while success:
        if count % 48 == 0:
            cv2.imwrite("film/frames-1997/frame-{}.jpg".format(count), image)
        success,image = vidcap.read()
        if not success:
            print('Read a new frame: ', success, ' ', count)
        count += 1
    
    
    return 0

if __name__ == '__main__':
    main()

