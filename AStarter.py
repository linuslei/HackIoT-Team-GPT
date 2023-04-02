from Crash_Detect import detect_crash
from cam_vid import start_recording
from ultrasonic import distance
import time
import paho.mqtt.client as mqtt

BROKER = 'test.mosquitto.org'
PORT = 1883

client = mqtt.Client()
client.connect(BROKER, PORT)
print(f"Connected to MQTT broker: {BROKER}")

while crash_flag == 0:
    crash_flag, accel, sound = detect_crash(1, 200)
    if crash_flag == 1:
        # start_recording()
        client.publish("crash_detect/crash_flag", crash_flag)
        client.publish("crash_detect/accelerometer", accel)
        client.publish("crash_detect/microphone_sensor", sound)
        # Publish to MQTT Upload to Amazon Cloud
