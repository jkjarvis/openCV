import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",image)
cv2.waitKey(0)

eq = cv2.equalizeHist(image)

cv2.imshow("original vs equalized",np.hstack([image,eq]))
cv2.waitKey(0)