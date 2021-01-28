import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("blur",image)

(T,thresh) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("thresh binary",thresh)

(T,threshInv) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh binary inv",threshInv)

cv2.imshow("Coins",cv2.bitwise_and(image,image,mask=threshInv))
cv2.waitKey(0)