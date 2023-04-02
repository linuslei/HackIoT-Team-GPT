import time
import paho.mqtt.client as mqtt
import socket
import base64
from picamera2 import Picamera2
from Crash_Detect import detect_crash

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

def start_recording():
    picam2.start_and_record_video("footage.mp4", duration = 10)

if __name__ == '__main__':
    ip_address=socket.gethostbyname(socket.gethostname())
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()
    time.sleep(1)
    while True:
       start_recording()
       crash_flag, accel, sound = detect_crash(accel_thres = 0.2, sound_thres = 200)
       print ("Crash flag: " + str(crash_flag))
       print ("acceleration: " + str(accel))
       print ("sound: " + str(sound))
       if crash_flag:
           picam2.stop_recording()
           print("the recording has stopped")
           chunk_size = 1024 * 1024  # 1 MB
           with open('footage.mp4', 'rb') as f:
               chunks = iter(lambda: f.read(chunk_size), b'')
               for i, chunk in enumerate(chunks):
                   chunk_base64 = base64.b64encode(chunk)
                   topic = 'crash_footage'
                   payload = {
                       'chunk_number': i,
                       'chunk_data': chunk_base64.decode('utf-8')
                   }
                   client.publish(topic, str(payload))
