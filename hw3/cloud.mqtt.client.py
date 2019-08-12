#!/usr/bin/env
import paho.mqtt.client as mqtt
import base64
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #client.subscribe("imagedata")
    client.subscribe("/image/#")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
def on_message(client, userdata, msg):
    print("msg topic: "+msg.topic)
    try:
        flname='/mybucket/cloud_decoded/'+msg.topic[7:]+".jpg"
        print(flname)
        f=open(flname, 'w+')
        f.write(base64.decodestring(msg.payload))
        f.close()
    except:
        print("failed to save")
    print "success"
j=0
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect("mosquitto2", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

