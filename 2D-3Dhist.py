import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)

fig = plt.figure()

chans = cv2.split(image)
colors = ('b','g','r')

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist,interpolation="nearest")
ax.set_title("2D color histogram for G and R")
plt.colorbar(p)



ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0],chans[2]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist,interpolation="nearest")
ax.set_title("2D color histogram for B and R")
plt.colorbar(p)
plt.show()

print("2D histogram shape: {} , with {} values".format(hist.shape,hist.flatten().shape[0]))

hist = cv2.calcHist([image], [0, 1, 2],None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
hist.shape, hist.flatten().shape[0]))

plt.show()