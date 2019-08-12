#!/usr/bin/env

import numpy as np
import cv2 as cv
#face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_cascade = cv.CascadeClassifier('/tmp/haarcascade_frontalface.xml')
img = cv.imread('/tmp/IMG_20190330_223243.jpg')
cv.imshow('img',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.3, 5)
i=0
for (x,y,w,h) in faces:
    i=2
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
if i==2:
   cv2.imwrite("face-" + str(i) + ".jpg", face)
    
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()

