import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

(B,G,R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B,G,R])
cv2.imshow("merged",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros(image.shape[:2],dtype="uint8")
cv2.imshow("red", cv2.merge([zeros,zeros,R]))
cv2.imshow("green", cv2.merge([zeros,G,zeros]))
cv2.imshow("blue", cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)