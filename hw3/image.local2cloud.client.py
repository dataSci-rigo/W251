#!/usr/bin/env
import paho.mqtt.client as mqtt



def on_connect_cloud(client, userdata, flags, rc):
    client.subscribe("/data/#")
    print("Cloud connected with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

    
def on_message_cloud(client, userdata, msg):
    #print("cloud"+msg.topic+" "+str(msg.payload))
    new_topic="/image/"+msg.topic[6:]+".jpg"
    print("new topic "+new_topic)
    r=cloud.publish(new_topic, payload=msg.payload, qos=2, retain=False)
    print "print result" +str(r)





cloud = mqtt.Client()
cloud.on_connect = on_connect_cloud
cloud.on_message = on_message_cloud
cloud.on_disconnect = on_disconnect
cloud.connect("mosquitto", 1883, 60)
#cloud.connect("52.117.25.20", 1883, 60)







# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
cloud.loop_forever()
