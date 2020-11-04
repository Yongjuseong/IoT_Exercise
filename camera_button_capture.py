import picamera
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
camera = picamera.PiCamera()
camera.resolution= (2592,1944) # Max Resolution
try:
	while True: #infinite Roop
		button_state = GPIO.input(12)
		if button_state == False: #Button push
			print('button pressed')
			time.sleep(2)
			camera.capture('example2.jpg')
			break
	time.sleep(0.2) # 0.2 seconds interval
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
