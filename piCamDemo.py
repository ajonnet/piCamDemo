from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import pi3d
from PIL import Image

camera=PiCamera()

rawCapture=PiRGBArray(camera)
time.sleep(0.5)
camera.capture(rawCapture, format="bgr")
camera.close()
cap_image=rawCapture.array

cv2.imwrite("Image.jpg",cap_image)
print("Image capture and written to disk")

DISPLAY = pi3d.Display.create(x=150, y=150, frames_per_second=20)
shader = pi3d.Shader("uv_flat")
im = Image.open("Image.jpg")
tex = pi3d.Texture(im)
sprite = pi3d.ImageSprite(tex,shader,w=100.0,h=100.0,z=5.0)


#sprite = pi3d.ImageSprite("textures/PATRN.PNG", shader, w=100.0, h=100.0, z=5.0)
mykeys = pi3d.Keyboard()

while DISPLAY.loop_running():
	sprite.draw()
	sprite.position(100,100,5.0)

	if mykeys.read() == 27:
		mykeys.close()
		DISPLAY.destroy()
		break
    
