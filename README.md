Crash Detect for Bike Share

-Input
 Accelerometer: detecting possible crash or fall
 Motion Sensor: detecting whether a person is onboard
 -GPS Sensor
  -For sending out location
 -Microphone Sensor
  -For detecting crash sound

-A crash is only identified if both sensors on the module

-Output
 -MQTT-Based reporting system
 -Two Scores
  -Confidence
  -Severity
 -Button on Website

Detecting Algorithm:
 -Accelerometer, Microphone Sensor sends and Heart Sensor, three must all comply so that a message can be sent
 -Requirements:
  -Accelerometer: Over a certain G value
  -Microphone:Sudden dramatic increase
  -Heart Sensor: An absence of heart rate in 15s

 -Confidence score and Severity score will be calculated based on data from Accelerometer, Microphone Sensor, and GPS sensor.
