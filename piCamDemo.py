from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera=PiCamera()
rawCapture=PiRGBArray(camera)

time.sleep(0.5)

camera.capture(rawCapture, format="bgr")
image=rawCapture.array

cv2.imwrite("Image.jpg",image)
print("Image capture and written to disk")
