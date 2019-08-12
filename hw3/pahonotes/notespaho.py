#!/usr/bin/env
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publishM

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
    #cloud.publish("image", payload="chekcing connection", qos=2, retain=False)
    #client.subscribe("image")
    client.subscribe("imagedata")

def on_connect_cloud(client, userdata, flags, rc):
    client.subscribe("image")
    #client.subscribe("imagedata")
    print("Cloud connected with result code "+str(rc))


def on_disconnect(client, userdata, rc):
    logging.info("disconnecting reason  "  +str(rc))
    client.connected_flag=False
    client.disconnect_flag=True

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

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
j=2

#client = mqtt.Client("local")
#client.on_connect = on_connect
#client.on_message = on_message
#client.on_disconnect = on_disconnect
client1.on_publish = on_publish 
#client.connect("mosquitto", 1883, 60)


cloud = mqtt.Client("cloud")
cloud.on_connect = on_connect_cloud
cloud.on_message = on_message
cloud.on_disconnect = on_disconnect
cloud.on_publish = on_publish 
cloud.connect("mosquitto", 1883, 60)
#cloud.connect("52.117.25.20", 1883, 60)
client.loop_start
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")
client.loop_stop() 

#cloud.publish("image", payload="/tmp/face-" + str(j) + ".jpg", qos=2, retain=False)






# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
cloud.loop_forever()

###########################
###########################
with BytesIO() as output:
    from PIL import Image
    with Image.open(filename) as img:
        img.convert('RGB').save(output, 'BMP')                
    data = output.getvalue()[14:]
