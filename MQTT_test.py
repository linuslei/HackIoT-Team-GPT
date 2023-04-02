from flask import Flask, render_template
import paho.mqtt.client as mqtt

# Create an instance of the Flask class
app = Flask(__name__)

BROKER = 'test.mosquitto.org'
PORT = 1883
TOPIC = 'mqtt/test'

# Define the MQTT topics to be used
accelerometer = "crash_detect/accelerometer"
sound = "crash_detect/microphone_sensor"
motion = "crash_detect/motion_sensor"
vision = "crash_detect/camera_sensor"
distance = "crash_detect/distance_sensor"
crash_flag = "crash_detect/crash_flag"


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

# Define the callback function for the MQTT client


def on_message(client, userdata, message):
    # subscribe to topics of interest here
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")


def crash_callback(client, userdata, message):
    if message.payload.decode() == 1:
        # if crash detected, add a button on the web page as an indicator
        print("Crash detected!")
        print("Are you okay?")


if __name__ == '__main__':
    # Set up the connection to the MQTT broker
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.subscribe("crash_detect/crash_flag")
    client.subscribe("crash_detect/accelerometer")
    client.subscribe("crash_detect/microphone_sensor")
    client.subscribe("crash_detect/motion_sensor")
    client.subscribe("crash_detect/camera_sensor")
    client.subscribe("crash_detect/distance_sensor")
    

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Disconnecting from broker...")
    client.disconnect()