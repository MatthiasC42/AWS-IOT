import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
def sendingfilecontent():
    file1 = open('28_jpg.txt', 'r')
    # Get next line from file
    line = file1.readline()
    print("Using for loop")
    for line in file1:
      count += 1
      print("Line{}: {}".format(count, line.strip()))
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
## Get next line from file
line = file1.readline()
line_split = line.split(' ')
print("Using for loop")
count = 0
for line in file1:
  count += 1
  myMQTTClient.publish(
        topic="home/helloworld",
        QoS=1,
        payload="Class:{} X:{} Y:{} Width:{} Height:{} ".format(count, line_split[0],line_split[1,line_split[2],line_split[3],ine_split[4])
        )
