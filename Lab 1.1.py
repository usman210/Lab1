from rasterio.plot import show
from PIL import Image


# reading tiff file
img1 = Image.open(r"E:\Usman\Image Processing\Peshawar\PeshawarHH.tif")
img2 = Image.open(r"E:\Usman\Image Processing\Peshawar\PeshawarHV.tif")
show(img1)
pixels = img1.load()
show(img2)
pixels = img2.load()