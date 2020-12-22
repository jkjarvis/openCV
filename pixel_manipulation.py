import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("image",image)
cv2.waitKey(0)

(b,g,r) = image[0,0]
print("b : {} , g: {} , r: {}".format(b,g,r))

img = image[0:100,0:100]
cv2.imshow("img",img)
cv2.waitKey(0)

# (b,g,r) = img
# print("b : {} , g: {} , r: {}".format(b,g,r))

image[0:100,0:100] = (0,255,0)
cv2.imshow("images",image)
cv2.waitKey(0)