
# from adafruit_mqtt import Adafruit_MQTT
# # mqtt=Adafruit_MQTT();
# # def reCallback(data):
# #     print("Du lieu nhan:", data);
# # mqtt.setCallback(reCallback);

# def custom_callback(data):
#     print("Custom Callback in main.py: " + data)
# # if __name__ == "__main__":
# mqtt_instance = Adafruit_MQTT()
# mqtt_instance.setCallback(custom_callback)

#     # Do other things or keep the program running
#     # while True:
#     #     pass

import sys
import time
import random
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "nutnhan1"
AIO_USERNAME = "ShangChi"
AIO_KEY = "aio_fpyf63s4Kesoi1QpEssan10yituO"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
 
while True:
    time.sleep(10)
    value = random . randint (0 , 100)
    print("Cap nhat: ", value)
    
    client.publish("cambien1",value)
