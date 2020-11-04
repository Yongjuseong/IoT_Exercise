import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
GPIO.setup(25,GPIO.OUT)

def buzz(): #buzzer function
	pitch = 1000 #pitch
	duration = 0.1 #duration
	period = 1.0/pitch # interval to make sound
	delay = period /2
	cycles = int(duration * pitch)

	for i in range(cycles):
		GPIO.output(25,True)
		time.sleep(delay)
		GPIO.output(25,False)
		time.sleep(delay)

try:
	while True:
		buzz() # buzzing!
		time.sleep(0.5) # 0.5 seconds interval

except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
