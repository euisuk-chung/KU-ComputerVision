# Assignment
## Task 1 : Implementing the Eigenvalue and Harris corner detectors
- Implement corner detectors based both on the minimum Eigenvalue and the Harrish measure. The corner detectors should be coded in a function called cornerDetect(img, winSize=7, type=0)

- The function should return the corner strength as a numpy array that has the same size as your input image. The steps the function has to do are:
    1. Filter img with Sobel kernel to obtain derivatives $$I_{x}$$, $$I_{y}$$
    2. For each pixel in img, determine second moment matrix H summed up over the window
    3. Depending on type, either determine the minimum eigenvalue using `numpy` functionality OR the Harris corner measure and store in return array

## Task 2 : Implementing the LoG scale blob detector 
- Implement the Laplacian of Gaussian blob detector including scale space tracking. For this, first write a function LoG(sigma=1,size=19), in which the first argument is the parameter of the Gaussian kernel and the second argument is the overall image size of the filter (here by default 19x19 pixels). 
- The function should return a numpy array with the filter values. At each pixel (x,y), the LoG has the value of (note, that the values have to be CENTERED in the window!!)

## Task 3 : Implement the solution to the heat equation for images
- Implement the numerical solution to the 2D heat equation using an image as the starting “temperature” L(i,j,n), where i,j index pixels and n indexes the time step.

---
# Result
- Task 1 [jupyter notebook](https://github.com/euisuk-chung/KU-ComputerVision/blob/main/Assignment3/corners.ipynb)
- Task 2 [jupyter notebook](https://github.com/euisuk-chung/KU-ComputerVision/blob/main/Assignment3/logscale.ipynb)
- Task 3 [jupyter notebook](https://github.com/euisuk-chung/KU-ComputerVision/blob/main/Assignment3/heatImage.ipynb)
