#!/usr/bin/env

#from ffnet import mlgraph, ffnet, tmlgraph, imlgraph
#import pylab
import sys
import cv2
import numpy
import base64
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


def transmitMQTT(strMsg, data):
    strMqttBroker = "mosquitto"
    strMqttChannel = "/data/"
    print('strMsg is: '+strMqttChannel+strMsg)
    print("success")
    retval, buffer = cv2.imencode('.jpg', data)
    jpg_as_text = base64.b64encode(buffer)
    publish.single(strMqttChannel+strMsg, jpg_as_text, hostname="mosquitto")
    f=open("/tmp/00proof3"+strMsg+".jpg","w+")
    f.write(base64.decodestring(jpg_as_text))
    f.close()



def facedetect():
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
   	    #cv2.imwrite("/tmp/face2-" + str(j) + ".jpg",frame)
            transmitMQTT("face2-" + str(j),frame)
	cv2.imshow("frame", frame)
        if (cv2.waitKey(1) == 0x1b) or (j>15):
	    cv2.destroyAllWindows()
            print 'ESC pressed. Exiting ...'
            break


if __name__ == "__main__":
    face_cascade = cv2.CascadeClassifier('/tmp/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(1)
    facedetect()
    

