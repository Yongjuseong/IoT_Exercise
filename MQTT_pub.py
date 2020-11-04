import paho.mqtt.client as mqtt

mqtt = mqtt.Client("python_pub") # mqtt client object
mqtt.connect("localhost", 1883) # mqtt server connect

mqtt.publish("IoT-P","led on") # Topic and message
mqtt.publish("IoT-P","led off")

mqtt.loop(2) # timeout 2 sec
