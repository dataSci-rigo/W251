#!/usr/bin/env
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publishM

def on_connect(client, userdata, flags, rc):
    print("Local Connected with result code "+str(rc))
    #cloud.publish("image", payload="chekcing connection", qos=2, retain=False)
    #client.subscribe("image")
    client.subscribe("imagedata")

def on_connect_cloud(client, userdata, flags, rc):
    client.subscribe("image")
    #client.subscribe("imagedata")
    print("Cloud connected with result code "+str(rc))


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

def on_message(client, userdata, msg):
    try:
        with open('Path/to/file', 'r') as content_file:
            content = content_file.read()
    except:
        print "fail"
    cloud.publish("imagedata", payload=content, qos=0, retain=False)
    print("local "+msg.topic+" "+str(msg.payload))
    
def on_message_cloud(client, userdata, msg):
    print("cloud"+msg.topic+" "+str(msg.payload))
j=2

#client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message
#client.on_disconnect = on_disconnect
#client.connect("mosquitto", 1883, 60)


cloud = mqtt.Client()
cloud.on_connect = on_connect_cloud
cloud.on_message = on_message
cloud.on_disconnect = on_disconnect
#cloud.connect("mosquitto", 1883, 60)
cloud.connect("52.117.25.20", 1883, 60)
#cloud.publish("image", payload="/tmp/face-" + str(j) + ".jpg", qos=2, retain=False)






# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
cloud.loop_forever()
