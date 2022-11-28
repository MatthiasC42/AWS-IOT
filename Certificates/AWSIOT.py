import os
import json
import time
import re
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Read text File
def read_text_file(file_path):
    with open(file_path, 'r') as line:  
        lines = line.readlines()
        line_split = lines.split(' ')
        data = json.dumps(getData(line_split))
        print(line_split)
        myMQTTClient.publish(
            topic="home/helloworld",
            QoS=1,
            payload=data
            )

def getData(line_split):
    data = {}
    data['class'] = float(line_split[1])
    data['x-cords'] = float(line_split[2])
    data['y-cords'] = float(line_split[3])
    data['width'] = float(line_split[4])
    data['height']= float(line_split[5])
    return data
myMQTTClient = AWSIoTMQTTClient("MatthiasClientID") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("apdgyoei7c8e7-ats.iot.us-east-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("AmazonRootCA1.pem",
 "aa90220f9da4a0f40df4fc8f4933f8ae68390740bedeb9067cd3bc78046dbb91-private.pem.key",
 "aa90220f9da4a0f40df4fc8f4933f8ae68390740bedeb9067cd3bc78046dbb91-certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()
#myMQTTClient.subscribe("home/helloworld", 1, helloworld)
#while True:
# time.sleep(5)
# Folder Path
path = "/home/ai/AWS-IOT/Certificates/test/labels"
# Change the directory
os.chdir(path)
print("Publishing Message from RPI")
print("Using for loop")
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
  
        # call read text file function
        read_text_file(file_path)
