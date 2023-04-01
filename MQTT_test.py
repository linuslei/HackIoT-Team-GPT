from flask import Flask, render_template
import paho.mqtt.client as mqtt

# Create an instance of the Flask class
app = Flask(__name__)

# Set up the connection to the MQTT broker
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

# Define the MQTT topics to be used
accelerometer = "crash_detect/accelerometer"
sound = "crash_detect/microphone_sensor"
motion = "crash_detect/motion_sensor"
vision = "crash_detect/camera_sensor"

# Define the initial state of the variables
accelerometer_state = ""
sound_state = ""
motion_state = ""
vision_state = ""

# Define the callback function for the MQTT client
def on_message(client, userdata, message):
    global accelerometer_state
    global sound_state
    global motion_state
    global vision_state
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
    if message.topic == accelerometer:
        accelerometer_state = str(message.payload.decode("utf-8"))
    elif message.topic == sound:
        sound_state = str(message.payload.decode("utf-8"))
    elif message.topic == motion:
        motion_state = str(message.payload.decode("utf-8"))
    elif message.topic == vision:
        vision_state = str(message.payload.decode("utf-8"))

# Set the callback function for the MQTT client
client.on_message = on_message

# Subscribe to the MQTT topics
client.subscribe(accelerometer)
client.subscribe(sound)
client.subscribe(motion)
client.subscribe(vision)

# Start the MQTT client loop
client.loop_start()

# Define a route for the index page
@app.route('/')
def index():
    global accelerometer_state
    global sound_state
    global motion_state
    global vision_state
    return render_template('index.html', accelerometer=accelerometer, sound=sound, motion=motion, vision=vision)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
