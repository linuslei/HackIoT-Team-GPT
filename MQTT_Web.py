import paho.mqtt.client as mqtt
import time

#Create an instance of the MQTT client and set up the connection to the MQTT broker
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

#Define the MQTT topics to be used
topic = "crash_detect/accelerometer"
topic2 = "crash_detect/motion_sensor"
topic3 = "crash_detect/microphone_sensor"

#Define the callback function to be used when a message is received
def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

#Set the callback function to be used when a message is received
client.on_message = on_message

#Subscribe to the MQTT topic
client.subscribe(topic)
client.subscribe(topic2)
client.subscribe(topic3)

#Loop to keep the program running
while True:
    client.loop()
    time.sleep(1)