import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow('Gaussian Blur',image)

canny = cv2.Canny(blur,100,180)
cv2.imshow('Canny',canny)
cv2.waitKey(0)

(cnts,_) = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print('Number of contours = {}'.format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins,cnts,-1,(0,255,0),2)
cv2.imshow('coins',coins)
cv2.waitKey(0)

for (i,c) in enumerate(cnts):
    (x,y,w,h) = cv2.boundingRect(c)

    print("coint #{}".format(i+1))
    coin = image[y:y+h,x:x+w]
    cv2.imshow("coin",coin)

    mask = np.zeros(image.shape[:2],dtype="uint8")
    ((centreX,centreY),radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask,(int(centreX),int(centreY)),int(radius),255,-1)
    mask = mask[y:y+h,x:x+w]
    cv2.imshow('masked coin',cv2.bitwise_and(coin,coin,mask=mask))
    cv2.waitKey(0)
