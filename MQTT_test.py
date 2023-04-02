from flask import Flask, render_template
import paho.mqtt.client as mqtt

# Create an instance of the Flask class
app = Flask(__name__)

# Define the MQTT topics to be used
accelerometer = "crash_detect/accelerometer"
sound = "crash_detect/microphone_sensor"
motion = "crash_detect/motion_sensor"
vision = "crash_detect/camera_sensor"
distance = "crash_detect/distance_sensor"

# Define the initial state of the variables
accelerometer_state = ""
sound_state = ""
motion_state = ""
vision_state = ""
distance_state = ""

# Define the latest message for each topic
accelerometer_message = ""
sound_message = ""
motion_message = ""
vision_message = ""
distance_message = ""

# Define the callback function for the MQTT client
def on_message(client, userdata, message):
    global accelerometer_state
    global sound_state
    global motion_state
    global vision_state
    global distance_state
    global accelerometer_message
    global sound_message
    global motion_message
    global vision_message
    global distance_message
    
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
    if message.topic == accelerometer:
        accelerometer_state = str(message.payload.decode("utf-8"))
        accelerometer_message = "Received accelerometer value: " + accelerometer_state
    elif message.topic == sound:
        sound_state = str(message.payload.decode("utf-8"))
        sound_message = "Received sound value: " + sound_state
    elif message.topic == motion:
        motion_state = str(message.payload.decode("utf-8"))
        motion_message = "Received motion value: " + motion_state
    elif message.topic == vision:
        vision_state = str(message.payload.decode("utf-8"))
        vision_message = "Received vision value: " + vision_state
    elif message.topic == distance:
        distance_state = str(message.payload.decode("utf-8"))
        distance_message = "Received distance value: " + distance_state

# Set up the connection to the MQTT broker
client = mqtt.Client()
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

# Subscribe to the MQTT topics
client.subscribe(accelerometer)
client.subscribe(sound)
client.subscribe(motion)
client.subscribe(vision)
client.subscribe(distance)

# Start the MQTT client loop
client.loop_start()

# Define a route for the index page
@app.route('/')
def index():
    global accelerometer_state
    global sound_state
    global motion_state
    global vision_state
    global distance_state
    global accelerometer_message
    global sound_message
    global motion_message
    global vision_message
    global distance_message

    return render_template('index.html', accelerometer=accelerometer_state, sound=sound_state, motion=motion_state, vision=vision_state, distance=distance_state, accelerometer_message=accelerometer_message, sound_message=sound_message, motion_message=motion_message, vision_message=vision_message, distance_message=distance_message)

# Run the Flask app
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)