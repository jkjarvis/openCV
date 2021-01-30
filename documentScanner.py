from skimage.filters import threshold_local
import cv2
import numpy as np
import argparse
import imutils
from transform import four_point_transform
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image,height=700)
cv2.imshow("original",image)
cv2.waitKey(0)

ratio = image.shape[0]/700.0
orig = image.copy()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image,(5,5),0)
edged = cv2.Canny(image,30,150)
cv2.imshow('Canny',edged)
cv2.waitKey(0)

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:5]


for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*peri,True)
    if len(approx) == 4:
        screenCnt = approx
        break

print('Finding contour of paper')
cv2.drawContours(image,[screenCnt],-1,(0,255,0),2)
cv2.imshow('Paper',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(screenCnt.shape)
warped = four_point_transform(orig,screenCnt.reshape(4,2) * ratio)


warped = cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
T = threshold_local(warped,13,offset=5,method='gaussian')
# T = cv2.adaptiveThreshold(warped,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,25)

warped = (warped > T).astype("uint8") * 255


print('Applying perspective transform')
cv2.imshow("original",imutils.resize(orig,height=650))
cv2.imshow('Converted',imutils.resize(warped,height=650))
cv2.waitKey(0)