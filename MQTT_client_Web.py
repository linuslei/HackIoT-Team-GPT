import paho.mqtt.client as mqtt
import time
import tkinter as tk

#Create an instance of the MQTT client and set up the connection to the MQTT broker
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

#Define the MQTT topics to be used
topic = "crash_detect/accelerometer"
topic2 = "crash_detect/motion_sensor"
topic3 = "crash_detect/microphone_sensor"

#Define the callback function to be used when a message is received
def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

#Set the callback function to be used when a message is received
client.on_message = on_message

#Subscribe to the MQTT topic
client.subscribe(topic)
client.subscribe(topic2)
client.subscribe(topic3)

#Create a Tkinter window
root = tk.Tk()
root.title("Crash Detection System")

#Create a label to display the received message
message_label = tk.Label(root, text="")
message_label.pack()

#Display the confidence and severity scores on a website and provide a button to report the crash.
def display():
    message_label.config(text="Confidence:" + str(confidence) + " Severity:" + str(severity))
    button = tk.Button(root, text="Report", command=report)
    button.pack()

#Report the crash to the emergency services
def report():
    print("Reported")

#Loop to keep the program runnings
while True:
    client.loop()
    root.update()
    time.sleep(1)
    if confidence > 0.5:
        display()


