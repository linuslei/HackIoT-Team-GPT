import paho.mqtt.client as mqtt
import time

#Create an instance of the MQTT client and set up the connection to the MQTT broker
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

#Define the MQTT topics to be used
accelerometer = "crash_detect/accelerometer"
sound = "crash_detect/microphone_sensor"
motion = "crash_detect/motion_sensor"
vision = "crash_detect/camera_sensor"


#Define the initial state of the light bulb
state = "OFF"
brightness = 0

#Define the callback function for the MQTT client
def on_message(client, userdata, message):
    global accelerometer
    global sound
    global motion
    global vision
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
    if message.topic == accelerometer:
        accelerometer = str(message.payload.decode("utf-8"))
    elif message.topic == sound:
        sound = str(message.payload.decode("utf-8"))
    elif message.topic == motion:
        motion = str(message.payload.decode("utf-8"))
    elif message.topic == vision:
        vision = str(message.payload.decode("utf-8"))

#Set the callback function for the MQTT client
client.on_message = on_message

#Subscribe to the MQTT topics
client.subscribe(accelerometer)
client.subscribe(sound)
client.subscribe(motion)
client.subscribe(vision)

#Start the MQTT client loop
client.loop_start()

#Main loop
while True:
    #Publish the state and brightness of the light bulb
    client.publish("crash_detect/accelerometer", accelerometer)
    client.publish("crash_detect/microphone_sensor", sound)
    client.publish("crash_detect/motion_sensor", motion)
    time.sleep(1)