from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import pi3d
from PIL import Image

cam_width = 128
cam_height = 112

camera = PiCamera()
camera.resolution = (cam_width,cam_height)
rawCapture=PiRGBArray(camera, size=(cam_width,cam_height))

time.sleep(1)

#camera.capture("Image.jpg")

#camera.capture(rawCapture, format="bgr")
#cap_image = rawCapture.array
#cv2.imwrite("Image.jpg",cap_image)

#camera.capture(rawCapture, format="bgr")
#camera.close()
#cap_image=rawCapture.array
#cv2.imwrite("Image.jpg",cap_image)
#print("Image capture and written to disk")


DISPLAY = pi3d.Display.create(x=10, y=150, frames_per_second=20)
shader = pi3d.Shader("uv_flat")
CAMERA = pi3d.Camera(is_3d=False)
mykeys = pi3d.Keyboard()

#im = Image.open("Image.jpg")
#tex = pi3d.Texture(im)
#sprite = pi3d.ImageSprite(tex,shader,w=100.0,h=100.0,z=5.0)
#sprite = pi3d.ImageSprite("textures/PATRN.PNG", shader, w=100.0, h=100.0, z=5.0)


while DISPLAY.loop_running():
	rawCapture.truncate(0)
	camera.capture(rawCapture, format="bgr", use_video_port=True)
	image = rawCapture.array;

	#camera.capture("Image.jpg")
	#camera.capture(rawCapture, format="bgr")
	#cap_image = rawCapture.array
	#cv2.imwrite("Image.jpg",cap_image)
	
	sprite = pi3d.ImageSprite(pi3d.Texture(image),shader,w=100.0,h=100.0,z=5.0)
	sprite.draw()
	sprite.position(100,100,5.0)
	
	if mykeys.read() == 27:
		mykeys.close()
		DISPLAY.destroy()
		camera.close()
		break