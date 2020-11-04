import picamera
camera = picamera.PiCamera()
camera.resolution = (1920,1080) # max resolution = 1080p
camera.start_recording('raspi_video.h264') # file name
camera.wait_recording(20) #20 seconds recording
camera.stop_recording()

