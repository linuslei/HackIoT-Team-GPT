from Body_Detect import read_pir_sensor
from Crash_Detect import detect_crash


pir_sensor_pin = 11
motion_detected = read_pir_sensor(pir_sensor_pin)

if motion_detected:
   crash_flag = detect_crash(1,200)
