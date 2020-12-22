import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

r = 150.0/image.shape[1]
dim = (100,int(image.shape[0]*r))

resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("resized",resized)
cv2.waitKey(0)