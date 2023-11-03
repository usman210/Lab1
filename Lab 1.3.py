from PIL import Image
import numpy as np
#open image
img1 = Image.open(r"E:\Usman\Image Processing\Peshawar\PeshawarHH.tif")
img2 = Image.open(r"E:\Usman\Image Processing\Peshawar\PeshawarHv.tif")

#convert image to numpy array
array1 = np.array(img1)
#Calculate the image statistics
mean = np.mean(array1)
std_dev = np.std(array1)
min = np.min(array1)
max = np.max(array1)

print("Statistics of HH")
print("Mean: ", mean)
print("Standard Deviation: ", std_dev)
print("Min: ", min)
print("Max: ", max)

width, height = img1.size
print("Width: ", width)
print("Height:", height)

#convert image to numpy array
array2 = np.array(img2)

#Calculate the image statistics
mean = np.mean(array2)
std_dev = np.std(array2)
min = np.min(array2)
max = np.max(array2)

print("\n Statistics of HV")
print("Mean of HVQ:", mean)
print("Standard Deviation: ", std_dev)
print("Min: ", min)
print("Max: ", max)

width, height = img2.size
print("Width: ", width)
print("Height: ", height)