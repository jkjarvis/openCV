import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

#average blur
blurred = np.hstack([
    cv2.blur(image,(2,2)),
    cv2.blur(image,(5,5)),
    cv2.blur(image,(7,7))
])

cv2.imshow("average blur",blurred)
cv2.waitKey(0)

#gaussian blur
gaussian = np.hstack([
    cv2.GaussianBlur(image,(3,3),0),
    cv2.GaussianBlur(image,(5,5),0),
    cv2.GaussianBlur(image,(7,7),0)
])

cv2.imshow("Gaussian blur",gaussian)
cv2.waitKey(0)

#median blur
median = np.hstack([
    cv2.medianBlur(image,3),
    cv2.medianBlur(image,5),
    cv2.medianBlur(image,7)
])

cv2.imshow("Median blur",median)
cv2.waitKey(0)

#bilateral blur
bilateral = np.hstack([
    cv2.bilateralFilter(image,5, 21, 21),
    cv2.bilateralFilter(image,7,31,31),
    cv2.bilateralFilter(image,9,41,41),
])

cv2.imshow("Bilateral Blur",bilateral)
cv2.waitKey(0)