import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("image",image)
cv2.waitKey(0)


image = imutils.resize(image,width=700)
cv2.imshow("resize",image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)

gray = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("gray blur",gray)
cv2.waitKey(0)

thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)[1]
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
thresh = cv2.erode(thresh,None,iterations=2)
cv2.imshow("erode",thresh)
cv2.waitKey(0)
thresh = cv2.dilate(thresh,None,iterations=2)
cv2.imshow("dilate",thresh)
cv2.waitKey(0)


cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts,key=cv2.contourArea)


extLeft = tuple(c[c[:,:,0].argmin()][0])
extRight = tuple(c[c[:,:,0].argmax()][0])
extTop = tuple(c[c[:,:,1].argmin()][0])
extBot = tuple(c[c[:,:,1].argmax()][0])


cv2.drawContours(image,[c],-1,(0,255,255),2)
cv2.circle(image,extLeft,8,(0,0,255),-1)
cv2.circle(image,extRight,8,(0,255,0),-1)
cv2.circle(image,extTop,8,(255,0,0),-1)
cv2.circle(image,extBot,8,(255,255,0),-1)

cv2.imshow("final",image)
cv2.waitKey(0)
