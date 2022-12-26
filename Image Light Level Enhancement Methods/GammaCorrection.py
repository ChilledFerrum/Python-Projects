import numpy as np
from src.Backend import Backend
import cv2 as cv


inputFolder = "input/"
outputFolder = "out/"

backend = Backend()


def GammaCorrectionMulti():
    Gamma = 2
    inverseGamma = 1 / Gamma
    for index, img in enumerate(backend.imagesBuffer):
        table = [((i / 255) ** inverseGamma) * 255 for i in range(256)]

        table = np.array(table, np.uint8)

        gammaCorrected = cv.LUT(img, table)
        backend.writeImages(index, gammaCorrected, backend.imageName[index])
    print("\n\nImage Filtering Complete. View outputGCmulti folder...")


def run():
    backend.setInputPath(inputFolder + "inputGC")
    backend.setOutPath(outputFolder + "outputGC")

    backend.run()
    GammaCorrectionMulti()


if __name__ == "__main__":
    run()
