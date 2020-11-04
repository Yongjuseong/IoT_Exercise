import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Button input setting
control = False #LED control static variable
try:
	while True:
		button_state=GPIO.input(12)
		if button_state == False: # push Button ==>False
			if control==True: # Toggle
				control=False
			else:
				control=True
				print('button pressed')
		if control ==True: #LED True-> turn on the LED
			GPIO.output(16,True)
		else:
			GPIO.output(16,False) #LED False-> turn off the LED
		time.sleep(0.2) #0.2 seconds interval
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
