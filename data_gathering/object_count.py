#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 29.01.2019 16:06:55 MSK

# Совокупность методов работы с контурами называется контурным анализом.

import sys
import numpy as np
import cv2 as cv

hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

def main():
    img = cv.imread('/home/boris/Видео/AK/film/frames-1997/frame-9840.jpg')
    #hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV 
    #thresh = cv.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    # ищем контуры и складируем их в переменную contours
    #contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blurred_image = cv.GaussianBlur(gray_image, (7,7), 0)
    
    #cv.imshow("Blurred image", blurred_image)
    
    #cv.waitKey()
    #cv.destroyAllWindows()
    
    canny = cv.Canny(blurred_image, 30, 100)
    #cv.imshow("Canny", canny)
    
    #cv.waitKey()
    #cv.destroyAllWindows()
    
    #contours, hierarchy= cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    contours, hierarchy= cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    #CHAIN_APPROX_NONE
    #CHAIN_APPROX_TC89_L1
    #CHAIN_APPROX_TC89_KCOS
    
    
    # отображаем контуры поверх изображения
    #print(contours)
    #print(hierarchy)
    
    print(len(contours))
    
    #cv.drawContours( img, contours, -1, (255,0,0), 3, cv.LINE_AA, hierarchy, 1 )
    #cv.imshow('contours', img) # выводим итоговое изображение в окно
    
    cv.drawContours(blurred_image, contours, -1, (0,255,0), 2)
    cv.imshow("objects Found", blurred_image)
    cv.waitKey()

    #cv.waitKey()
    cv.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    main()

