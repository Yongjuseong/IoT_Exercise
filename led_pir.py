import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

try:
	while True:
		if GPIO.input(24) == True: # sensor -> True
			print("SEONSOR ON!!")
			GPIO.output(16,True) # Turn on LED
			time.sleep

		if GPIO.input(24) == False: # Sensor -> False
			print("SEONSOR OFF!!")
			GPIO.output(16,False) # Turn off LED
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
