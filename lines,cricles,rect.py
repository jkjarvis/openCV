import cv2
import numpy as np

canvas = np.zeros((300,300,3),dtype="uint8")
cv2.imshow("canvas",canvas)
cv2.waitKey(0)

green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green,1)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)

red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red,20)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)

cv2.rectangle(canvas,(0,0),(60,60),red)
cv2.imshow("red rect",canvas)
cv2.waitKey(0)

cv2.rectangle(canvas,(250,0),(190,60),green,3)
cv2.imshow("green rect",canvas)
cv2.waitKey(0)

blue=(255,0,0)
cv2.rectangle(canvas,(250,250),(300,300),blue,-1)
cv2.imshow("blue rect",canvas)
cv2.waitKey(0)

canvas = np.zeros((300,300,3),dtype="uint8")
(centerX,centerY) = canvas.shape[1]//2,canvas.shape[0]//2

for r in range(0,175,25):
    cv2.circle(canvas,(centerX,centerY),r,(255,255,255))
cv2.imshow("circles",canvas)
cv2.waitKey(0)

for i in range(0,25):
    radius = np.random.randint(0,high=200)
    color = np.random.randint(0,high=256,size=(3,)).tolist()
    pos = np.random.randint(0,300,size=(2,))
    cv2.circle(canvas,tuple(pos),radius,color,-1)

cv2.imshow("circles",canvas)
cv2.waitKey(0)