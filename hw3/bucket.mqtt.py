#!/usr/bin/env
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("imagedata")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
def on_message(client, userdata, msg):
    j=j+1
    file = open('face'+str(j)+".txt", 'w+')
    f.write(msg.topic+" "+str(msg.payload))
    f.close()
    print(msg.topic+" "+str(msg.payload))
j=0
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect("mosquitto", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
