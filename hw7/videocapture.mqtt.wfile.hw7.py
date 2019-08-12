#!/usr/bin/env

#from ffnet import mlgraph, ffnet, tmlgraph, imlgraph
#import pylab
import sys
import cv2
import numpy
import base64
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import face_recognition

#platform.machine() == "aarch64"

def transmitMQTT(strMsg, data):
    strMqttBroker = "mosquitto"
    strMqttChannel = "/data/"
    print('strMsg is: '+strMqttChannel+strMsg)
    print("success")
    retval, buffer = cv2.imencode('.jpg', data)
    jpg_as_text = base64.b64encode(buffer)
    publish.single(strMqttChannel+strMsg, jpg_as_text, hostname="mosquitto")



def facedetect():
    j=0
    while 1:
        _,frame =cam.read()
	
        image_faces = []
	small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
	rgb_small_frame = small_frame[:, :, ::-1]
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_recognition.face_locations(rgb_small_frame)
	
 	#faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 	if faces!=[]:
	    j=j+1
	    for (top, right, bottom, left) in faces:
		top *= 4
           	right *= 4
            	bottom *= 4
            	left *= 4

            	# Draw a box around the face
            	cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    		#roi_gray = gray[y:y+h, x:x+w]
    		#roi_color = frame[y:y+h, x:x+w]
		print "face found"
   	    cv2.imwrite("/tmp/face2-" + str(j) + ".jpg",frame)
            #transmitMQTT("face2-" + str(j),frame)
	cv2.imshow("frame", frame)
        if (cv2.waitKey(1) == 0x1b) or (j>15):
	    cv2.destroyAllWindows()
            print 'ESC pressed. Exiting ...'
            break


if __name__ == "__main__":
    #face_cascade = cv2.CascadeClassifier('/tmp/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(1)
    facedetect()
    

