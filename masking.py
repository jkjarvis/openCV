import cv2
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

M = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
Mask = cv2.rectangle(M, (cX - 75, cY - 75), (cX + 75, cY + 75),255,-1)
cv2.imshow("Mask", Mask)

image2 = cv2.bitwise_and(image,image,mask=Mask)
cv2.imshow("Masked",image2)
cv2.waitKey(0)


