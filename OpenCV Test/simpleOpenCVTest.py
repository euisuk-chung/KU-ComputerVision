import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/ishihara_9.png', cv2.IMREAD_UNCHANGED)

print("OpenCV version:  {0}".format(cv2.__version__))
print("Image shape: {0}".format(img.shape))
print('Press key 0 to exit')


cv2.imshow('Ishihara Test Plate | Shape: {0} | OpenCV Version: {1}'.format(img.shape,cv2.__version__),img)
cv2.waitKey(0)
