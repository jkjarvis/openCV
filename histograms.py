from matplotlib import pyplot as plt
import cv2
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

hist = cv2.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title("Gray Scale histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

chans = cv2.split(image)
colors = ('b','g','r')
plt.figure()
plt.title("Flattened color histograms")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for (chan, color) in zip(chans,colors):
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color=color)
    plt.xlim([0,256])

plt.show()