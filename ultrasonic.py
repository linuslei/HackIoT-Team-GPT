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

	Start = time.time()
	Stop = time.time()
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        Start = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        Stop = time.time()
 
    # time difference between start and arrival
    Duration = Stop - Start
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = Duration * 17150
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()