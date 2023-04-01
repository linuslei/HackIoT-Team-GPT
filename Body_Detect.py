#Detect the presence of a human getting on our bicycle

# set the Sensitivity to minimum (3 meters) and the Time delay to minimum (3 seconds)

# Way Zheng: HC-SR501 PIR motion sensor

import RPi.GPIO as GPIO
import time

"""
to call thie function, use the following code:

from pir_sensor import read_pir_sensor

pir_sensor_pin = 11
motion_detected = read_pir_sensor(pir_sensor_pin)

if motion_detected:
    print("Motion detected!")
else:
    print("No motion detected.")

"""

def read_pir_sensor(pir_sensor_pin):
    GPIO.setmode(GPIO.BOARD)

    # Set up PIR sensor input pin
    GPIO.setup(pir_sensor_pin, GPIO.IN)

    print("PIR sensor warming up...")
    time.sleep(10)  # allow sensor to warm up

    print("PIR sensor ready")
    try:
        while True:
            if GPIO.input(pir_sensor_pin):
                return True  # motion detected!
            time.sleep(0.5)  # wait for half a second before checking again
    except KeyboardInterrupt:
        GPIO.cleanup()



