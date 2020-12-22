import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

Gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
LAB = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)

cv2.imshow("Gray",Gray)
cv2.imshow("HSV",HSV)
cv2.imshow("LAB",LAB)
cv2.waitKey(0)
