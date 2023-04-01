#Detect Crash

import time
import board
import busio
import adafruit_mpu6050

#Use MPU6050 to detect crash
#A crash is defined as a sudden change in acceleration
#The MPU6050 is a 6-axis accelerometer and gyroscope
#The accelerometer measures acceleration in 3 axes
#The gyroscope measures angular velocity in 3 axes

#TODO:Read the accelerometer data, Write it as a function
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






