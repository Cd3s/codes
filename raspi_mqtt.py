import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

def on_connect(client, userdata, rc,properties=None):
    print ("Connected with rc: " + str(rc))
    client.subscribe("exp7/led")

def on_message(client, userdata, msg):
    print ("Topic: "+ msg.topic+"\nMessage:"+str(msg.payload))
    if b"1" in msg.payload:
        print("  Green on!")
        GPIO.output(11, True)
        
    if b"0" in msg.payload:
        print("  Green off!")
        GPIO.output(11, False)
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

client.loop_forever()

