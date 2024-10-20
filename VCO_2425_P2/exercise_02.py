"""
@file     exercise_02.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Simple image transformations.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import math
import matplotlib.pyplot as plt
import numpy as np  
from PIL import Image

# ---------------------------------------------------------------------------- #
# GLOBAL FUNCTIONS

def checkboard(grid= 10, square_size = 10):
    """
    Function to return a Checkerboard graylevel
    image of n x n squares each of size 'sz'.
    """
    print("Checkerboard pattern:")
 
    # create a n * n matrix
    x = np.zeros((grid, grid), dtype = np.uint8)
 
    # fill with 255 the alternate rows and columns
    x[1::2, ::2] = 255
    x[::2, 1::2] = 255
    
    sz = grid * square_size 
    size = (sz,sz)
    img = Image.fromarray(x, mode='L')
    img_res = img.resize(size, resample=Image.Resampling.NEAREST)
    
    return img_res

    ### end def checkboard() ###

# ---------------------------------------------------------------------------- #
# EXERCISE 2.1

# Create 10 x 10 squares checkboard
image_2_1 = checkboard(10, 10)

# Showing image_2_1 in a window using Matplotlib
plt.imshow(np.asarray(image_2_1))

# Show the image
plt.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 2.2

# Create 10 x 10 squares checkboard
image_2_2 = checkboard(10, 10)

# Set matplotlib figure size
plt.figure(figsize=(12,4))

# Showing image_2_2 in a window using Matplotlib
plt.subplot(121) # On the left
plt.imshow(np.asarray(image_2_2))

# Calculate sin and cos of +10 degree
angle = 30
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))

# Translation matrix
T_translate = np.array([
    [1, 0, 100],
    [0, 1,  50],
    [0, 0,   1]])

# Rotation matrix
T_rotate = np.array([
    [cos, -sin, 0],
    [sin,  cos, 0],
    [  0,    0, 1]])

# Create the inverse transform matrix (Image.transform uses the inverse)
T = T_translate @ T_rotate
T_inv = np.linalg.inv(T)

# Aply T_inv matrix to image_2_2
image_2_2_transformed = image_2_2.transform((230, 230),
                                            Image.Transform.AFFINE,
                                            data=T_inv.flatten()[:6],
                                            resample=Image.NEAREST)

# Showing image_2_2_transformed in a window using Matplotlib
plt.subplot(122) # On the right
plt.imshow(np.asarray(image_2_2_transformed))

# Show the image
plt.show()

# end of file #
