#!/usr/bin/env
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    client.subscribe("image")
    client.subscribe("imagedata")
    print("Local Connected with result code "+str(rc))

def on_connect_cloud(client, userdata, flags, rc):
    print("Cloud connected with result code "+str(rc))
    client.subscribe("image")
    client.subscribe("imagedata")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
def on_message(client, userdata, msg):
    j=j+1
    print("local "+msg.topic+" "+str(msg.payload))
    #cloud.publish("imagedata", payload="/tmp/face-" + str(j) + ".jpg", qos=2, retain=False)
    
def on_message_cloud(client, userdata, msg):
    print("cloud"+msg.topic+" "+str(msg.payload))
j=2

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("mosquitto", 1883, 60)
print "connced??"

#cloud = mqtt.Client()
#cloud.on_connect = on_connect_cloud
#cloud.on_message = on_message_cloud
#cloud.on_disconnect = on_disconnect

#cloud.connect("52.117.25.20", 1883, 60)







# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
