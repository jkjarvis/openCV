import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

print("max : {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min : {}".format(cv2.subtract(np.uint8([200]),np.uint8([200]))))
print("numpy add : {}".format(np.uint8([200])+np.uint8([100])))
print("numpy sub : {}".format(np.uint8([100])-np.uint8([200])))

M = np.ones(image.shape,dtype="uint8")*100
added = cv2.add(image,M)
cv2.imshow("added",added)
cv2.waitKey(0)

M = np.ones(image.shape,dtype="uint8")*50
subtract = cv2.subtract(image,M)
cv2.imshow("subtract",subtract)
cv2.waitKey(0)