#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 29.01.2019 16:50:11 MSK

import cv2

def main():
    #image = cv2.imread('/home/boris/Видео/AK/film/frames-1997/frame-9216.jpg') #!
    #image = cv2.imread('/home/boris/Видео/AK/film/frames-1997/frame-11088.jpg') #!
    #image = cv2.imread('/home/boris/Видео/AK/film/frames-1997/frame-12144.jpg') # <
    #
    image = cv2.imread('/home/boris/Видео/AK/film/frames-1997/frame-25248.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cascadePath = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascadePath)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (30,30))
    print("Found {0} faces!".format(len(faces)))
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(x, y, w, h)
        #print(y)
        
    cv2.imshow("Faces found" ,image)
    cv2.waitKey(0)
    
    return 0

if __name__ == '__main__':
    main()

