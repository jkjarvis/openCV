import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

horizontal = cv2.flip(image,1)
cv2.imshow("horizontal",horizontal)
# cv2.waitkey(0)

vertical = cv2.flip(image,0)
cv2.imshow("vertical",vertical)
# cv2.waitKey(0)

both = cv2.flip(image,-1)
cv2.imshow("both flip", both)
cv2.waitKey(0)

crop = image[10:100,20:150]
cv2.imshow("cropped",crop)
cv2.waitKey(0)