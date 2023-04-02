from ultrasonic import distance
from Crash_Detect import detect_crash
from cam_vid import start_recording
import time
import paho.mqtt.client as mqtt
import subprocess
import sys

BROKER = 'test.mosquitto.org'
PORT = 1883

client = mqtt.Client()
client.connect(BROKER, PORT)
print(f"Connected to MQTT broker: {BROKER}")

crash_flag = 0
btn = 0
t = 0



while True:
    crash_flag, accel, sound = detect_crash(1.1, 200)
    diff_distance = distance()
    print("accel: " + str(accel))
    if crash_flag == 1:
        start_recording()
        confidence = accel / 1+ sound / 200+ diff_distance / 20
        severity = accel*5 + sound/150
        print("Crash detected! Are you OK?")
        print("Press 1 to confirm that you're OK")
        btn = input()
        if btn == 1:
            print("Thank you for confirming that you're OK")
        while t < 15 and btn != 1:
            t = t + 1
            print("You have " + str(15 - t) + " seconds to confirm that you're OK")
            time.sleep(1)
        if btn != 1:
            print("We have called 911 for you.")
            client.publish("crash_detect/crash_flag", "Crash detected!")
            client.publish("crash_detect/scores", "Confidence: " + str(confidence)+ " Severity: " + str(severity))
    time.sleep(0.1)




