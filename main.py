<<<<<<< HEAD
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
=======
#Main program

# Set up an interrupt function that will trigger when the accelerometer detects a sudden increase in acceleration or the microphone sensor detects a loud sound.

# The interrupt function will then trigger the crash detection function.

# The crash detection function will then trigger the buzzer and the LED to flash.

# The crash detection function will also trigger the camera to take a picture and save it to the SD card.

# The crash detection function will also trigger the GPS to record the location of the crash.

# The crash detection function will also trigger the accelerometer to record the acceleration of the crash.

# The crash detection function will also trigger the microphone to record the sound of the crash.

# The crash detection function will also trigger the temperature sensor to record the temperature of the crash.

# The crash detection function will also trigger the humidity sensor to record the humidity of the crash.

# The crash detection function will also trigger the pressure sensor to record the pressure of the crash.

# The crash detection function will also trigger the light sensor to record the light of the crash.
>>>>>>> d4253d3e1a3bc7925bad27ed4c2e40c1a83f8eb7
