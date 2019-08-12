#!/usr/bin/env

#from ffnet import mlgraph, ffnet, tmlgraph, imlgraph
#import pylab
import sys
import cv2
import numpy



if __name__ == "__main__":
    face_cascade = cv2.CascadeClassifier('/tmp/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(1)
    j=0
    while 1:
        _,frame =cam.read()
	
        image_faces = []
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 	if faces!=():
	    j=j+1
	    for (x,y,w,h) in faces:
    		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    		roi_gray = gray[y:y+h, x:x+w]
    		roi_color = frame[y:y+h, x:x+w]
		print "face found"
   	    cv2.imwrite("/tmp/face-" + str(j) + ".jpg",frame)
	cv2.imshow("frame", frame)
        if (cv2.waitKey(1) == 0x1b) or (j==8):
            print 'ESC pressed. Exiting ...'
            break
