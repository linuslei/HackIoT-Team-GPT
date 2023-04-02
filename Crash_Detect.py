#Detect Crash
import paho.mqtt.publish as publish

#Notice: Wiring CLK = 11 MISO = 9 MOSI = 10 CS = 8
import time
import board
import busio
import adafruit_mpu6050
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import numpy as np
from Body_Detect import read_pir_sensor


#Use MPU6050 to detect crash
#A crash is defined as a sudden change in acceleration
#The MPU6050 is a 6-axis accelerometer and gyroscope
#The accelerometer measures acceleration in 3 axes
#The gyroscope measures angular velocity in 3 axes

#Read the accelerometer data, Write it as a function
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mpu6050.MPU6050(i2c)

def read_accel():
    #Read the accelerometer data, translate it to G value
    #Return the acceleration in 3 axes
    #The accelerometer measures acceleration in m/s^2
    #The accelerometer measures acceleration in 3 axes
    #The accelerometer measures acceleration in 3 axes
    accel_x, accel_y, accel_z = sensor.acceleration
    accel_x = accel_x / 9.8
    accel_y = accel_y / 9.8
    accel_z = accel_z / 9.8
    return accel_x, accel_y, accel_z

def read_sound():
    CLK = 11
    MISO = 9
    MOSI = 10
    CS = 8
    mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
    analog_value = mcp.read_adc(0)
    return analog_value

def detect_crash(accel_thres, sound_thres):
    accel_x,accel_y,accel_z = read_accel()
    sound = read_sound()
    abs_accel = np.sqrt(accel_x**2 + accel_y**2 + accel_z**2)
    if abs_accel > accel_thres and sound > sound_thres:
        crash_flag = 1
    else:
        crash_flag = 0

    # Publish the crash flag value to the MQTT broker
    publish.single("crash_detect/crash_flag", crash_flag, hostname="test.mosquitto.org")

    return crash_flag, abs_accel, sound

##For testing
while True:
    crash_flag, accel, sound = detect_crash(accel_thres = 0.2, sound_thres = 200)
    print(crash_flag)
    print(accel)
    print(sound)
    time.sleep(0.1)





