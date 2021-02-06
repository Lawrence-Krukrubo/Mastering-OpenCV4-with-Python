import numpy as np
import cv2

# Set a universal seed for this notebook
# Reproducibility


def seed(seeds=31415):
    np.random.seed(seeds)


seed()

img = cv2.imread('logo.png')
im_shape = img.shape  # (Rows, Columns, Channel or No_Channel for Gray or B&W)
im_ndim = img.ndim
im_size = img.size  # (multiply all values in shape)
im_dtype = img.dtype   # The image data  type

print(f'Shape is: {im_shape}\nNdim is: {im_ndim}\nSize is: {im_size}\nDtype is: {im_dtype}')

cv2.imshow('original-image', img)

cv2.waitKey(0)