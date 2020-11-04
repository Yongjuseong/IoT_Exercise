import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) # LED R
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Button
GPIO.setup(24,GPIO.IN) # PIR
GPIO.setup(25,GPIO.IN) # BUZZER
GPIO.setup(25,GPIO.OUT) #BUZZER

control =  0 #control static variable

def buzz():   #function for buzzer
	pitch = 1000 # frequency
	duration = 0.1 # time 
	period = 1.0 / pitch # interval
	delay = period /2 # delay
	cycles = int(duration * pitch)

	for i in range(cycles):
		GPIO.output(25,True)
		time.sleep(delay)
		GPIO.output(25,False)
		time.sleep(delay)
try:
	while True:
		if GPIO.input(24) == True:
			print("SENSOR ON !")
			control = 1

		if control ==1:
			while True:
				GPIO.output(16,True)
				buzz()
				if GPIO.input(12)==True:
					GPIO.output(16,False)
					control = 0
					break
				time.sleep(0.3)
		time.sleep(0.3)

except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
