#!/usr/bin/env
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import time



strMqttBroker = "57.117.25.20"
strMqttChannel = "imagedata"
broker="mosquitto"
topic="image"
        




def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
    publish.single(strMqttChannel, message.payload, hostname=strMqttBroker)



while True:
    time.sleep(.5)
    subscribe.callback(on_message_print, topic, hostname=broker, qos=0)
    time.sleep(.5)

