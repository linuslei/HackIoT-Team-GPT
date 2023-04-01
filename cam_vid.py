import time

from picamera2 import Picamera2

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

picam2.start_and_record_video("test.mp4", duration = 10)
