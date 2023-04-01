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

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
 
    # time difference between start and arrival
    duration = stop_time - start_time
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = duration * 17150
 
    return distance
 