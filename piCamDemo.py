from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import pi3d

camera=PiCamera()
rawCapture=PiRGBArray(camera)

time.sleep(0.5)

camera.capture(rawCapture, format="bgr")
image=rawCapture.array

#cv2.imwrite("Image.jpg",image)
#print("Image capture and written to disk")

shader = pi3d.Shader("uv_flat")

im = Image.fromarray(image)
tex = pi3d.Texture(im)
sprite = pi3d.ImageSprite(tex,shader,w=100.0,h=100.0)
DISPLAY = pi3d.Display.create(x=150, y=150, frames_per_second=20)

#sprite = pi3d.ImageSprite("textures/PATRN.PNG", shader, w=100.0, h=100.0, z=5.0)
mykeys = pi3d.Keyboard()

while DISPLAY.loop_running():
    sprite.draw()
    sprite.position(100,100,5.0)

    if mykeys.read() == 27:
        mykeys.close()
        DISPLAY.destroy()
    break
    