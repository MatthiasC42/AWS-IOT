import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def helloworld(self, params, pocket):
 print('Recieved message')
 print('Topic: ' + packet.topic)
 print("Payload: ", (packet.payload))
myMQTTClient = AWSIoTMQTTClient("RishabClientID") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("apdgyoei7c8e7-ats.iot.us-east-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/AWS-IoT/Certificates/AmazonRootCA1.pem",
 "/AWS-IoT/Certificates/60b1321bad028ee4d96d2706b6a6783eccf6e45a3583cb50a63ab579a2042611-private.pem.key",
 "/AWS-IoT/Certificates/60b1321bad028ee4d96d2706b6a6783eccf6e45a3583cb50a63ab579a2042611-certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()
myMQTTClient.subscribe("home/helloworld", 1, helloworld)