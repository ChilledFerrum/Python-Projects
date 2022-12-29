# Various Data visualization methods of Images
[![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) <br/>


### Description:
This algorithm uses various data visualization techniques to visualize an image's light conditions and color variation differences. <br/>
This algorithm was originally created for the use of image data visualization primarily for my thesis, but I'm also leaving it as open source for other people to explore and use. No citations are required, although it would be highly appreciated if the tool was citated in the references for others to use. <br/>
2 of the sample images are provided from the [ExDark dataset](https://github.com/cs-chan/Exclusively-Dark-Image-Dataset).

### Features:
 - [x] Sobel Derivatives
 - [x] Contour Maps
 - [x] 3D Image Graphing (On a top Down view)
 - [x] Image Color Channel Extraction
 - [x] Histogram Graphs for each Color Channel (RGB only)

### Samples:
<table>
<th>Input</th><th>Output</th>
<tr>
<td><img src="https://github.com/ChilledFerrum/Python/blob/49acd0aed8e7d6dace0ae3a1a959b0c7e68e8a78/Image%20Data%20Visualization/input/2015_02453.jpg" width="385" height="289"></td>
<td><strong>3D Map</strong> (The real image output is tighter and clearer)<br/><img src="https://github.com/ChilledFerrum/Python/blob/49acd0aed8e7d6dace0ae3a1a959b0c7e68e8a78/Image%20Data%20Visualization/output/3D/3D_2015_02453.jpg" width="385" height="289"></td>
</tr>

<tr>
<td><img src="https://github.com/ChilledFerrum/Python/blob/6b59b4673d74c2562374d4e37c4975bed71c2570/Image%20Data%20Visualization/input/2015_05757.jpg" width="375" height="400"></td>
<td><strong>Contours</strong> (The real output does not contain the axis)<br/><img src="https://github.com/ChilledFerrum/Python/blob/6b59b4673d74c2562374d4e37c4975bed71c2570/Image%20Data%20Visualization/output/contours/Contour_2015_05757.jpg" width="375" height="400"></td>
</tr>

<tr>
<td><img src="https://github.com/ChilledFerrum/Python/blob/6b59b4673d74c2562374d4e37c4975bed71c2570/Image%20Data%20Visualization/input/IMG_4813.jpg" width="375" height="289"></td>
<td><strong>Sobel Derivatives</strong><br/><img src="https://github.com/ChilledFerrum/Python/blob/6b59b4673d74c2562374d4e37c4975bed71c2570/Image%20Data%20Visualization/output/sobel/Sobel_IMG_4813.jpg" width="375" height="289"></td>
</tr>
</table> <br/>

## Requirements:
OpenCV, numpy, matplotlib, python


## Compile:
```
> pip install numpy
> pip install matplotlib
```
Check out the OpenCV website to setup the package into your interpreter and run the program.
```
> python imageDataVisualization.py
```

### Optional Citation

#### BibTex
```
@software{ImageDataVisualization,
author = {Dimitrios Mpouziotas},
title = {Various Image Data Visualization Methods using OpenCV \& Python},
url = {https://github.com/ChilledFerrum/Python/tree/main/Image%20Data%20Visualization},
year = {2022},
month = {12}
}
```

#### APA
```
Dimitrios M. (2022). Various Image Data Visualization Methods using OpenCV \& Python [Computer software]. https://github.com/ChilledFerrum/Python/tree/main/Image%20Data%20Visualization
```
