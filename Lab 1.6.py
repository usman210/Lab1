import matplotlib.pyplot as plt
import numpy as np
import cv2

#trnslating matrix of HHQ
#shifting by (100,50)
M = np.float32([[1, 0, 100], [0 , 1, 50]])
try:
    img1 = cv2.imread(r"E:\Usman\Image Processing\Peshawar\PeshawarHH.tif")
    transmat1 = cv2.warpAffine(img1, M, (100, 50))
    cv2.imwrite("Translated1.tiff", img1)
    plt.imshow(transmat1)
    plt.title("Translated")
    plt.show()
except IOError:
    print("error")

#trnslating matrix of HvQ
try:
    img2 = cv2.imread(r"E:\Usman\Image Processing\Peshawar\PeshawarHV.tif")
    transmat2 = cv2.warpAffine(img2, M, (100, 50))
    cv2.imwrite("Translated2.tiff", img2)
    plt.imshow(transmat2)
    plt.title("Translated")
    plt.show()
except IOError:
    print("error")