import matplotlib.pyplot as plt
import cv2

try:
    # Read the image from disk
    img1 = cv2.imread(r"E:\Usman\Image Processing\Peshawar\PeshawarHH.tif")

    # Get the dimensions of the image
    (height, width) = img1.shape[:2]

    # Specify the size of the resized image along with the interpolation method.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC is used for zooming.
    rsize1 = cv2.resize(img1, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)

    # Write the resized image back to disk with the correct file name and extension
    cv2.imwrite("Resized1.tif", rsize1)  # Replace with the appropriate extension (.jpg, .png, etc.)
    
    # Display the resized image
    plt.imshow(cv2.cvtColor(rsize1, cv2.COLOR_BGR2RGB))  # OpenCV uses BGR, so convert to RGB for matplotlib
    plt.title("Resized")
    plt.show()
except IOError:
    print("Error while reading or writing the image file!")

#Resizing HV
try:
    #read image from disk
    img2 = cv2.imread(r"E:\Usman\Image Processing\Peshawar\PeshawarHV.tif")

    #get no of pixel horizontally and vertically
    (height, width) = img2.shape[:2]

     # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC is used for zooming.
    resize2 = cv2.resize(img2, (int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)

    #write the image back to disk
    cv2.imwrite("Resized2.tif", resize2)
    plt.imshow(resize2)
    plt.title("Resized")
    plt.show()
except IOError:
    print("Error while reading tiff file!!!")