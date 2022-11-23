import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

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
count = 0
print("Publishing Message from RPI")
myMQTTClient.publish(
file1 = open('28_jpg.txt', 'r')  
while True:
    count += 1
  
    # Get next line from file
    line = file1.readline()
  
    # if line is empty
    # end of file is reached
    if not line:
        break
    topic="home/helloworld",
    QoS=1,
    payload=("Line{}: {}".format(count, line.strip()))
  
file1.close()
)
