from RPLCD.i2c import CharLCD
import Adafruit_DHT
import time

dht_type = 11 # DHT type
bcm_pin = 23 # pin number
lcd = CharLCD('PCF8574',0x27)

try:
	while True:
		time.sleep(3)
		lcd.clear()
		humidity, temperature = Adafruit_DHT.read_retry(dht_type,bcm_pin)
		humid = str(round(humidity,1))
		temp = str(round(temperature,1))
		print(temp,humid)
		lcd.write_string('TEMP ')
		lcd.write_string(temp)
		lcd.crlf()
		lcd.write_string('HUMID ')
		lcd.write_string(humid)
		lcd.write_string('% ')
except KeyboardInterrupt:
	lcd.clear()
