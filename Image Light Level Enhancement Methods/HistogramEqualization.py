from src.Backend import Backend
import cv2 as cv
import numpy as np


inputFolder = "input/"
outputFolder = "out/"

backend = Backend()

def histogramEqualizationMulti():
    for index, img in enumerate(backend.imagesBuffer):
        b, g, r = cv.split(img)
        h_b, bin_b = np.histogram(b.flatten(), 256, [0, 256])
        h_g, bin_g = np.histogram(g.flatten(), 256, [0, 256])
        h_r, bin_r = np.histogram(r.flatten(), 256, [0, 256])
        # calculate cdf
        cdf_b = np.cumsum(h_b)
        cdf_g = np.cumsum(h_g)
        cdf_r = np.cumsum(h_r)

        # mask all pixels with value=0 and replace it with mean of the pixel values
        cdf_m_b = np.ma.masked_equal(cdf_b, 0)
        cdf_m_b = (cdf_m_b - cdf_m_b.min()) * 255 / (cdf_m_b.max() - cdf_m_b.min())
        cdf_final_b = np.ma.filled(cdf_m_b, 0).astype('uint8')

        cdf_m_g = np.ma.masked_equal(cdf_g, 0)
        cdf_m_g = (cdf_m_g - cdf_m_g.min()) * 255 / (cdf_m_g.max() - cdf_m_g.min())
        cdf_final_g = np.ma.filled(cdf_m_g, 0).astype('uint8')
        cdf_m_r = np.ma.masked_equal(cdf_r, 0)
        cdf_m_r = (cdf_m_r - cdf_m_r.min()) * 255 / (cdf_m_r.max() - cdf_m_r.min())
        cdf_final_r = np.ma.filled(cdf_m_r, 0).astype('uint8')
        # merge the images in the three channels
        img_b = cdf_final_b[b]
        img_g = cdf_final_g[g]
        img_r = cdf_final_r[r]

        img_out = cv.merge((img_b, img_g, img_r))
        # validation
        equ_b = cv.equalizeHist(b)
        equ_g = cv.equalizeHist(g)
        equ_r = cv.equalizeHist(r)
        equ = cv.merge((equ_b, equ_g, equ_r))
        backend.writeImages(index, equ, backend.imageName[index])

    print("\n\nImage Filtering Complete. View outputHE folder...")


def run():
    backend.pathInput = inputFolder + "inputHE"
    backend.pathOutput = outputFolder + "outputHE"
    backend.run()

    histogramEqualizationMulti()


if __name__ == "__main__":
    run()
