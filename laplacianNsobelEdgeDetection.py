import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

lap = cv2.Laplacian(image,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian',lap)
cv2.waitKey(0)