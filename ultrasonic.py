import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
    duration = stop_time - start_time
    distance = duration * 17150 #34330(speed of sound in cm)/2(back and forth)
 
    return distance
 
def dist_diff():
    dist_pre = distance()
    sleep(0.5)
    dist_curr = distance()
    dist_diff = dist_curr-dist_pre()
    return dist_diff
