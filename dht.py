import Adafruit_DHT
import time
dht_type = 11 #Type of DHT
dht_pin = 23 # DHT Pin number

while True:
	humidity,temperature = Adafruit_DHT.read_retry(dht_type,dht_pin) # Get values from DHT
	
	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f} C Humidity{1:0.1f}%'.format(temperature,humidity))
	
	time.sleep(3)
