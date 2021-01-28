import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

sobelX = cv2.Sobel(image,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX,sobelY,)
cv2.imshow("SobelX",sobelX)
cv2.imshow("SobelY",sobelY)
cv2.imshow('sobel',sobelCombined)
cv2.waitKey(0)