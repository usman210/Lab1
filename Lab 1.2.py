import rasterio
import matplotlib.pyplot as plt

img1 = rasterio.open(r"E:\Usman\Image Processing\Peshawar\PeshawarHH.tif")
img2 = rasterio.open(r"E:\Usman\Image Processing\Peshawar\PeshawarHV.tif")

#HH
width = img1.width
height = img1.height
print("Width x Height is", width, 'x', height)
n_bands = img1.count
print("Number of Band: ", n_bands)
img1.width
img1.height
img1.count
plt.imshow(img1.read(1))
plt.show()
img1.close()

#HV
width = img2.width
height = img2.height
print("Size (Width x Height) is", width, 'x', height)
n_bands = img2.count
print("Number of Bands: ", n_bands)
img2.width
img2.height
img2.count
plt.imshow(img2.read(1))
plt.show()
img2.close()