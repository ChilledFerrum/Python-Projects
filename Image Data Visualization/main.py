import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

inputDirectory = "input/"
outputDirectory = "output/"

files = os.listdir(inputDirectory)
for fileName in files:

    filepath = inputDirectory + fileName

    image = cv.imread(filepath, cv.IMREAD_UNCHANGED)

    # Get DPI data for correct Image Scaling
    try:
        imagedpi = Image.open(filepath).info['dpi']
    except KeyError:
        # Default DPI if image is jfif format
        imagedpi = [72, 72]

    # Converts the Image into the L*a*b* Color formatted image
    imlab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
    height, width, depth = image.shape

    print("Image Resolution: ", width, "x", height)
    print("Generating Data image: ", fileName)

    # ================================== SPLIT IMAGE TO RGB COLOR CHANNELS ==================================
    blueChanel = image[:, :, 1]
    greenChannel = image[:, :, 1]
    redChannel = image[:, :, 2]

    blueImg = np.zeros(image.shape)
    greenImg = np.zeros(image.shape)
    redImg = np.zeros(image.shape)

    blueImg[:, :, 0] = blueChanel
    greenImg[:, :, 1] = greenChannel
    redImg[:, :, 2] = redChannel

    cv.imwrite(outputDirectory+"rgb/"+"B_"+fileName, blueImg)
    cv.imwrite(outputDirectory+"rgb/"+"G_"+fileName, greenImg)
    cv.imwrite(outputDirectory+"rgb/"+"R_"+fileName, redImg)

    # ================================== Generate Contours ==================================
    y = range(image.shape[0])
    x = range(image.shape[1])

    # Rotate image to correspond to the same rotation as the contour map
    rotated = cv.rotate(image, cv.ROTATE_180)
    rotated = cv.flip(rotated, 1)

    # Pre-set figure size to correspond to the image's size with DPI
    fig = plt.figure(figsize=(width/imagedpi[0], height/imagedpi[0]), dpi=imagedpi[0])

    # Remove the axis information to correspond the entire plot's size as the image size
    plt.axis('off')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Tighten the layout and make the padding = 0 to correspond the image size
    plt.tight_layout(pad=0)

    # Plot the contours as a 3D graph in a 2D form
    X, Y = np.meshgrid(x, y)
    plot = plt.contour(X, Y, rotated[:, :, 0], 50)

    plt.savefig(outputDirectory + "contours/" + "Contour_" + fileName)
    fig.clf()

    # ================================== CREATE 3D IMAGE PLOT FIGURE ==================================
    fig = plt.figure(3)

    ax = plt.axes(projection='3d')

    y = range(imlab.shape[0])
    x = range(imlab.shape[1])
    X, Y = np.meshgrid(x, y)

    ax.plot_surface(X[::-1], Y[::-1], imlab[::-1, ::-1, 0], cmap='jet')
    ax.view_init(azim=90, elev=90)
    plt.title("Top Down View of the 3D Image")
    plt.savefig(outputDirectory+"3D/"+"3D_" +fileName, bbox_inches="tight")

    fig.clf()
    # ================================== SOBEL DERIVATIVES OF IMAGE ==================================
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
    src = cv.GaussianBlur(image, (3, 3), 0)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)

    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    cv.imwrite(outputDirectory+"sobel/"+"Sobel_" + fileName, grad)

    # ================================== HISTOGRAMS OF IMAGE  ==================================
    plt.figure()
    b, g, r = cv.split(image)
    colorList = ('b', 'g', 'r')

    channels = image.shape[2]
    if channels > 1:
        for i, col in enumerate(colorList):
            histr = cv.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
            plt.title("Image " + fileName + " Histogram")
            plt.xlabel("Intensity Value Range")
            plt.ylabel("Intensity Value Count")

        plt.savefig(outputDirectory+"histograms/" + 'Histogram_' + fileName)
    print("Generating Data image: ", fileName, " - done\n")
    fig.clf()
