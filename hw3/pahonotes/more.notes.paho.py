

import paho.mqtt.client as mqtt
def Initialise_clients(cname):
    #callback assignment
    client= mqtt.Client(cname,False) #don't use clean session
    if mqttclient_log: #enable mqqt client logging
        client.on_log=on_log
    client.on_connect= on_connect        #attach function to callback
    client.on_message=on_message        #attach function to callback
    client.on_subscribe=on_subscribe
	#flags set
    client.topic_ack=[]
    client.run_flag=False
    client.running_loop=False
    client.subscribe_flag=False
    client.bad_connection_flag=False
    client.connected_flag=False
    client.disconnect_flag=False
    return client


Example code:
import paho.mqtt.client as paho
broker="192.168.1.184"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("house/bulb1","on")  




#####################
def wait_for(client,msgType,period=0.25):
 if msgType=="SUBACK":
  if client.on_subscribe:
    while not client.suback_flag:
      logging.info("waiting suback")
      client.loop()  #check for messages
      time.sleep(period)
#####################

def on_message(client, userdata, message):
    print("message received  ",str(message.payload.decode("utf-8")),\
          "topic",message.topic,"retained ",message.retain)
    if message.retain==1:
        print("This is a retained message")


########################################
import time
import paho.mqtt.client as paho
broker="broker.hivemq.com"
broker="iot.eclipse.org"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
strMqttBroker = "57.117.25.20"
strMqttChannel = "imagedata"
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    print('strMsg is:')
    print("success")
    publish.single(strMqttChannel, strMsg, hostname=strMqttBroker) 

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
