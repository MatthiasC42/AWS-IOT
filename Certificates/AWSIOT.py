import json
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
def getData(line_split):
    data = {}
    data['class'] = float(line_split[0])
    data['x-cords'] = float(line_split[1])
    data['y-cords'] = float(line_split[2])
    data['width'] = float(line_split[3])
    data['height']= float(line_split[4])
    return data
def helloworld(self, params, packet):
 print('Recieved message')
 print('Topic: ' + packet.topic)
 print("Payload: ", (packet.payload))
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
print("Publishing Message from RPI")
file1 = open('28_jpg.txt', 'r')
print("Using for loop")
count = 0
for line in file1:
  line_split = line.rstrip("\n").split(' ')
  count += 1
  data = json.dumps(getData(line_split))
  print(data)
  myMQTTClient.publish(
        topic="home/helloworld",
        QoS=1,
        payload=data
        )
