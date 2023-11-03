import cv2
import matplotlib.pyplot as plt

try:
    # Read image from disk.
    img1 = cv2.imread(r"E:\Usman\Image Processing\Peshawar\PeshawarHH.tif")
     # Shape of image in terms of pixels.
    (rows, cols) = img1.shape[:2]
    # getRotationMatrix2D creates a matrix needed for transformation.
    # We want matrix for rotation w.r.t center to 45 degree without scaling.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    rotate1 = cv2.warpAffine(img1, M, (cols, rows))
 
    # Write image back to disk.
    cv2.imwrite('Rotate1.tiff', rotate1)
    plt.imshow(rotate1)
    plt.title("Rotated")
    plt.show()
 
except IOError:
    print('Error while reading files !!!')

try:
    # Read image from disk.
    img2 = cv2.imread(r"E:\Usman\Image Processing\Peshawar\PeshawarHV.tif")
 
     # Shape of image in terms of pixels.
    (rows, cols) = img2.shape[:2]
 
    # getRotationMatrix2D creates a matrix needed for transformation.
    # We want matrix for rotation w.r.t center to 45 degree without scaling.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    rotate2 = cv2.warpAffine(img2, M, (cols, rows))
 
    # Write image back to disk.
    cv2.imwrite('result.tiff', rotate2)
    plt.imshow(rotate2)
    plt.title("Rotated")
    plt.show()
 
except IOError:
    print('Error while reading files !!!')