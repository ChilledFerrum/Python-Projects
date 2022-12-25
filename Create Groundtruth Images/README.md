# Groundtruth annotation algorithm for the ExDark dataset
[![PWC](https://img.shields.io/badge/Dataset-ExDark%20Repository-brightgreen?url=https://github.com/cs-chan/Exclusively-Dark-Image-Dataset&logo=Github)](https://github.com/cs-chan/Exclusively-Dark-Image-Dataset)
[![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) <br/>
## Description:
The purpose of this algorithm is to visualize the groundtruth images given by the ExDark dataset. It embeds the groundtruth information from the '.txt' files into the images and allows the user to visualize the groundtruth images. It works by drawing bounding-boxes around the classified objects within the dataset.<br/><br/>
This algorithm is supported for the ExDark dataset and was primarily created for applied research in my thesis and research paper.
<img src="https://github.com/ChilledFerrum/Python/blob/6b309f2ff83276dc385bd90a09b1fb0d56ec5eb6/Create%20Groundtruth%20Images/Assets/Exdark.gif"/>
## Requirements:
#### OpenCV, ExDark dataset
#### Recommended file tree 

- src
> - main.py
> - Groundtruth_Images
> - ExDark
>> - dataset
>> - Groundtruth

By having the correct setup as seen above and running main.py, the program will begin to generate the images with the bounding boxes of each object in the ExDark dataset.

## Citation:
```
@article{Exdark,
  title={Getting to Know Low-light Images with The Exclusively Dark Dataset},
  author={Loh, Yuen Peng and Chan, Chee Seng},
  journal={Computer Vision and Image Understanding},
  volume={178},
  pages={30-42},
  year={2019},
  doi={https://doi.org/10.1016/j.cviu.2018.10.010}
}
```
