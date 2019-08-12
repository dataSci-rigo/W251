#!/usr/bin/env
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import time
import base64

#mqtt.enable_logger(logger=log1.txt)

strMqttBroker = "57.117.25.20"
strMqttBroker = "mosquitto"
strMqttChannel = "imagedata"
broker="mosquitto"
topic="image"
for j in range(7):
	time.sleep(0.5)
	with open("/tmp/face-" + str(j+1) + ".jpg", "rb") as imageFile:
		payload = base64.b64encode(imageFile.read())
		print "complete decoding"
	payload=str(j+5)
   	publish.single(strMqttChannel, payload, hostname=strMqttBroker,keepalive=0.5, port=1883)
