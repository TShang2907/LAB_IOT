
# from adafruit_mqtt import Adafruit_MQTT
# # mqtt=Adafruit_MQTT();
# # def reCallback(data):
# #     print("Du lieu nhan:", data);
# # mqtt.setCallback(reCallback);


import sys
import time
import random
from Adafruit_IO import MQTTClient
#from ai import *
from uart import *

AIO_FEED_ID1 = "nutnhan1"
AIO_FEED_ID2 = "nutnhan2"
AIO_USERNAME = "ShangChi"
AIO_KEY = "aio_eKeo09dEO2jWl4KhMDlIlNV0nQsD"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID1)
    client.subscribe(AIO_FEED_ID2)


def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    
    if (feed_id=="nutnhan1"):
        print("Nut nhan 1 : " + payload)
        if (payload=="0"):
            writeData("1:0")
        else :
            writeData("1:1")
    if (feed_id=="nutnhan2"):
        print("Nut nhan 2 : " + payload)
        if (payload=="0"):
            writeData("2:0")
        else :
            writeData("2:1")
            
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter_ai=3

while True:
    # counter_ai=counter_ai-1
    # if counter_ai<=0:
    #     counter_ai=3
    #     ai_result=image_detector()
    #     print("AI Output:",ai_result)
    #     client.publish("ai",ai_result)
    readSerial(client)
    time.sleep(1)


 