#!/usr/bin/env
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time



strMqttBroker = "57.117.25.20"
strMqttChannel = "imagedata"
def on_connect(client, userdata,flags, rc):
    print "connect success"
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    print('strMsg is:')
    print("receive success")
    publish.single(strMqttChannel, message.payload, hostname=strMqttBroker)
    reconnect_delay_set(min_delay=0.5, max_delay=5) 
client = mqtt.Client("client")
client.on_connect = on_connect
client.on_message = on_message
#client.on_disconnect = on_disconnect
#client.on_publish = on_publish 

broker="mosquitto"
topic="image"
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("topic")#subscribe
time.sleep(2)
#publish
while True:
    time.sleep(1)
client.disconnect() #disconnect
client.loop_stop() #stop loop
