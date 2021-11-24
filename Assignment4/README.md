# Assignment
## Task 1 : Stitching images
- Go outside the science library onto the grass and take 10 pictures of the campus, taking care that each picture overlaps with the other, but that you also cover some large area. 

- `loadImages`: Load images, convert them to double and to grayscale. Return list of images.
- `getFeaturePoints`: Detect feature points in an image, using the (Harris) corner detector you developed in Assignment 3. Save them in a list and return. The function should also plot the detected feature points in the image.

- `getFeatureDescriptors`: For a given input list of feature points, extract its neighborhood using the pixel values in a small window around each point as a feature vector. The window size needs to be a parameter of the function. Return the feature vectors as another list.

- `match2Images`: Given lists of feature points and feature descriptors from two images, match them. For this, compute distances between every descriptor in one image and every descriptor in the other image – Euclidean distance may work, but more robust matching can be done with normalized cross correlation (look it up, it’s easy!) of the descriptors. Implement both ways and check later which gives better results. Select matches based on the ratio criterion with a suitable threshold (this is a function parameter). The function should also plot the matches between the two images. Return the matches as a list of indices in the two images.

- `refineMatches`: Given lists of feature points and the match list, implement RANSAC to estimate a homography mapping one image onto the other (so, the full number of 8 parameters). In each iteration of RANSAC, simply select 4 points at random, estimate the homography by finding the nullspace of the transform (see lecture 6!). This function also needs parameters for inlier thresholds and rounds of iterations with which you need to experiment. Return the estimated homography. When running the function, it should print out the number of inliers that survive RANSAC and the average residual for the inliers (squared distance between the point coordinates in one image and the transformed coordinates of the matching point in the other image). Finally, the function should plot the surviving matches.

- `warpImages`: given a list of homographies and a list of n images, warp images 2-n onto the image space of image 1. For this, you are allowed to use the OpenCV function warpPerspective, which will work with your estimated homography (take care though in which direction you estimated the homography!!). In the function you will need to first create a new image big enough to hold all stitched images and then use warpPerspective to composite the two images into it. Use averaging of pixels for the stitching. Return the full stitched image and have the function also plot the result. Implement all functions with

---
# Result
- Task 1 [jupyter notebook](https://github.com/euisuk-chung/KU-ComputerVision/blob/main/Assignment4/stiching.ipynb)