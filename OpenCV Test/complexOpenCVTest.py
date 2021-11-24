# do the standard imports
import numpy as np
import cv2 as cv
import time

# we are going to try to check whether we can detect a face
# in the input stream, so this code initializes two types
# of detectors that already come with OpenCV, a full-face
# detector and an eye-detector
facedet = cv.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
eyedet = cv.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')

# open some video capture source from webcam
cap = cv.VideoCapture(-1)

# note you can simply change this to do offline processing 
# by putting in a filename instead like this:
# open some video capture source using a file from disk
# cap = cv.VideoCapture("../data/videos/dance.mp4")

# now that we've opened the capture source, let's get
# some information from it, like frame width and height
fw = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
fh = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# we want to draw some text for user information, so we
# have to initialize OpenCV's rather complicated font management
font                   = cv.FONT_HERSHEY_SIMPLEX
# where to draw the text - here we make use of the frame height
bottomLeftCornerOfText = (10,int(fh)-20)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

# do we want face detection?
doFaceDetect = True

# read the first frame of the capture source
# the picture is actually returned as the second value
_, frame1 = cap.read()
# convert frame to grayscale
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
# make output image encoding optic flow as hsv image
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
# as long as we receive frames from capture source
while(1):
    start = time.time()
    # read next frame and convert to grayscale
    _, frame2 = cap.read()
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    
    # this does the whole magic - dense estimation of optic flow
    # with some "sensible" parameters
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    # this splits the flow components into magnitude and angle
    mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
    # angle (optic flow direction) is encoded as hue
    hsv[...,0] = ang*180/np.pi/2
    # magnitude is encoded as brightness
    hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    # and convert this into BGR for visualization
    bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
    if doFaceDetect:
        # now do face detection - for this, we need the original frame in color
        faces = facedet.detectMultiScale(frame2, 1.3, 5)
        for (x,y,w,h) in faces:
            bgr = cv.rectangle(bgr,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = next[y:y+h, x:x+w]
            roi_color = frame2[y:y+h, x:x+w]
            eyes = eyedet.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                bgr = cv.rectangle(bgr,(ex+x,ey+y),(ex+ew+x,ey+eh+y),(0,255,0),2)
        cv.putText(bgr,'{:}x{:}@{:.2f}fps - {:} faces'.format(fw,fh,1/(time.time()-start),len(faces)),bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
    else:
        cv.putText(bgr,'{:}x{:}@{:.2f}fps - no face detection'.format(fw,fh,1/(time.time()-start)),bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
    cv.imshow('frame2',bgr)
    # wait for key press or escape key for max 30s
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('f'):
        doFaceDetect = not(doFaceDetect)
    # start with next frame as baseline
    prvs = next
# release the capture device and close all windows
cap.release()
cv.destroyAllWindows()