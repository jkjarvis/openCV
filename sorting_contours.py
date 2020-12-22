import cv2
import argparse
import imutils
import numpy as np

def sort_contours(cnts, method="L2R"):
    reverse = False
    i=0

    if method == "R2L" or method == "B2T":
        reverse = True
    
    if method == "T2B" or method == "B2T":
        i=1
    
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
		key=lambda b:b[1][i], reverse=reverse))

    return (cnts, boundingBoxes)

def draw_contour(image, c,i):
    
    M = cv2.moments(c)
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])

    cv2.putText(image, "#{}".format(i+1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
    return image


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, help="path to input image")
ap.add_argument("-m","--method",required=True,help="sorting method")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# image - imutils.resize(image, height=600)
accumEdged = np.zeros(image.shape[:2], dtype="uint8")


for chan in cv2.split(image):
    chan = cv2.medianBlur(chan, 11)
    edged = cv2.Canny(chan, 50, 200)
    accumEdged = cv2.bitwise_or(accumEdged, edged)

cv2.imshow("edged map", accumEdged)
cv2.waitKey(0)

cnts = cv2.findContours(accumEdged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
orig = image.copy()
# loop over the (unsorted) contours and draw them
for (i, c) in enumerate(cnts):
	orig = draw_contour(orig, c, i)
# show the original, unsorted contour image
cv2.imshow("Unsorted", orig)
# sort the contours according to the provided method
(cnts, boundingBoxes) = sort_contours(cnts, method=args["method"])
# loop over the (now sorted) contours and draw them
for (i, c) in enumerate(cnts):
	draw_contour(image, c, i)
# show the output image
cv2.imshow("Sorted", image)
cv2.waitKey(0)