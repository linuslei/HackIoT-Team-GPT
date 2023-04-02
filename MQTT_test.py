from flask import Flask, render_template
import paho.mqtt.client as mqtt
import base64
#from Crash_Detect import detect_crash

# Create an instance of the Flask class
app = Flask(__name__)

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
    #subscribe to topics of interest here
    client.subscribe("crash_detect/accelerometer")
    client.subscribe("crash_detect/microphone_sensor")
    client.subscribe("crash_detect/motion_sensor")
    client.subscribe("crash_detect/camera_sensor")
    client.subscribe("crash_detect/distance_sensor")
    client.subscribe("crash_detect/crash_flag")
    client.message_callback_add("crash_detect/crash_flag", crash_callback)

"""def crash_callback(client, userdata, message):
    if message.payload.decode() == 1:
        #if crash detected, add a button on the web page as an indicator
        return render_template('index.html', button=True)"""

# Define a route for the index page
@app.route('/')
def index():
    # Set the initial state of the sensors
    accelerometer_state = "Unknown"
    sound_state = "Unknown"
    motion_state = "Unknown"
    vision_state = "Unknown"
    distance_state = "Unknown"
    # Set the initial message for the sensors
    return render_template('index.html', accelerometer=accelerometer_state, sound=sound_state, motion=motion_state, vision=vision_state, distance=distance_state, button=False)

if __name__ == '__main__':
    # Set up the connection to the MQTT broker
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("test.mosquitto.org", 1883, 60)
    # Start the MQTT client loop
    client.loop_start()
    #app.run(host='192.168.64.6', port=5000)
    app.run(host='0.0.0.0', port=5000)