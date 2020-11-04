from picamera import PiCamera
import time

camera = PiCamera() # Call PiCamera object
camera.start_preview() # preview on

time.sleep(10)
camera.stop_preview() # preview off
