Crash Detect for Bike Share

-Input
 
Accelerometer: detecting possible crash or fall by speed

Motion Sensor: detecting whether a person is onboard

Microphone Sensor: detecting crash sound

-Definition

a crash is only identified if both sensors on the module

-Output
 
1. MQTT-Based reporting system

2. Two Scores

3. Confidence
 
4. Severity

5. Button on Website

-Detecting Algorithm
 
Accelerometer, Microphone Sensor sends and Heart Sensor, three must all comply so that a message can be sent

-Requirements
 
Accelerometer: Over a certain G value

Microphone:Sudden dramatic increase

Heart Sensor: An absence of heart rate in 15s

Confidence score and Severity score will be calculated based on data from Accelerometer, Microphone Sensor, and GPS sensor.
