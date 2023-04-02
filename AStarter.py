
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

crash_flag = 0
btn = 0

while True:
    crash_flag, accel, sound = detect_crash(1, 200)
    if crash_flag == 1:
        start_recording()
        print("Crash detected! Are you OK?")
        btn = input("Press 1 to confirm that you're OK")
        while t != 15 and btn != 1:
            t = t + 1
            print("You have " + str(15 - t) + " seconds to confirm that you're OK")
            time.sleep(1)
        if btn != 1:
            print("We have called 911 for you.")
            client.publish("crash_detect/crash_flag", "Crash Happened to User")  




