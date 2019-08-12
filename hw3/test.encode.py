#!/usr/bin/env

import base64
while True:
	fil=input()
	with open("/tmp/"+str(fil), "rb") as imageFile:
	    str1 = base64.b64encode(imageFile.read())
	    #print str1
	#jpg_as_text = base64.b64encode(open("/tmp/face-159.jpg","rb").read())
	#publish.single(strMqttChannel+strMsg, jpg_as_text, hostname="mosquitto")
	f=open("/tmp/17proof3"+str(fil)+".gif","w+")
	f.write(base64.decodestring(str1))
	f.close()
