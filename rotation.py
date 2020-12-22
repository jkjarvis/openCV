import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

(h,w) = image.shape[:2]
center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,45,1)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("rotated",rotated)
cv2.waitKey(0)
