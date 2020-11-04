
import paho.mqtt.client as mqtt
# callback when getting COUNTACK response from server
def on_connect(client,userdata, falges, rc):
	print("Connected with result code " +str(rc))
	client.subscribe("IoT-P") # subscribe IoT-P

# Callback wehn getting publish message from server
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload)) # print topic and message

client = mqtt.Client() # Client object
client.on_connect = on_connect # callback setup
client.on_message = on_message # callback setup

client.connect("localhost",1883,60) # Connect with MQTT broker
client.loop_forever()

