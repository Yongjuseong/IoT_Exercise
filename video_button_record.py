import picamera
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
camera = picamera.PiCamera()
camera.resolution = (1920,1080) # Max reslolution = 1080p

try:
	while True:
		button_state = GPIO.input(12) # button push
		if button_state ==False:
			print('button pressed')
			camera.start_recording('raspi_button.h264') # save file as
			camera.wait_recording(15) #15 seconds recording
			camera.stop_recording()
			break
		time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
