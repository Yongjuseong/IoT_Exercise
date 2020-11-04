from picamera import PiCamera

import time

camera = PiCamera()

camera.resolution = (2592,1944) # Max resolution

time.sleep(2) # interval 2 seconds

camera.capture('example.jpg') # save as example.jpg)
