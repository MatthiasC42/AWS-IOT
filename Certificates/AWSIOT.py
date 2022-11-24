import json
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
def getNormalHeartRate(line_split):
    data = {}
    data['class'] = line_split[0]
    data['x-cords'] = line_split[1]
    data['y-cords'] = line_split[2]
    data['width'] = line_split[3]
    data['height']= line_split[4]
    return data
def helloworld(self, params, packet):
 print('Recieved message')
 print('Topic: ' + packet.topic)
 print("Payload: ", (packet.payload))
myMQTTClient = AWSIoTMQTTClient("MatthiasClientID") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("au37ws9t6r3g5-ats.iot.ap-southeast-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("AmazonRootCA1.pem",
 "589d76ddf0c89b03d80bdf0a02e10d046b0c5ab0571a9ae5c5e249319dc4a7c2-private.pem.key",
 "589d76ddf0c89b03d80bdf0a02e10d046b0c5ab0571a9ae5c5e249319dc4a7c2-certificate.pem.crt")

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
file1 = open('29_jpg.txt', 'r')
print("Using for loop")
count = 0
for line in file1:
  line_split = line.split(' ')
  count += 1
  data = json.dumps(getNormalHeartRate(line_split))
  myMQTTClient.publish(
        topic="home/helloworld",
        QoS=1,
        payload=data
        )
