import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #BCM 16
GPIO.setup(20,GPIO.OUT) #BCM 20
GPIO.setup(21,GPIO.OUT) #BCM 21
try:
	while True:
		GPIO.output(16,True) # 16 On
		time.sleep(0.1) #0.1 seconds interval
		GPIO.output(16,False) # 16 Off
		time.sleep(0.1)
		GPIO.output(20,True) # 20 ON
		time.sleep(0.1)
		GPIO.output(20,False) # 20 Off
		time.sleep(0.1)
		GPIO.output(21,True) # 21 ON
		time.sleep(0.1)
		GPIO.output(21,False) # 21 Off
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
