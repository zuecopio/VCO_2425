"""
@file     exercise_01.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Combining image transformations.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import math
import matplotlib.pyplot as plt
import numpy as np  
from PIL import Image

# ---------------------------------------------------------------------------- #
# EXERCISE 1.1

# Reading a file, image_1_1
image_1_1 = Image.open("../vco_images/student_images/building4.JPG")

# Showing image_1_1 in a window using Matplotlib
plt.imshow(np.asarray(image_1_1))

# Show the image
plt.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 1.2

# Read a file, image_1_2
image_1_2 = Image.open("../vco_images/student_images/building4.JPG")

# Set matplotlib figure size
plt.figure(figsize=(12,4))

# Show image_1_2 in a window using Matplotlib
plt.subplot(121) # On the left
plt.imshow(np.asarray(image_1_2))

# Calculate sin and cos of +10 degree
angle = 10
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))

# Rotation matrix
T_rotate = np.array([
    [cos, -sin, 0],
    [sin,  cos, 0],
    [  0,    0, 1]])

# Create the inverse transform matrix (Image.transform uses the inverse)
T = T_rotate
T_inv = np.linalg.inv(T)

# Aply T_inv matrix to image_1_2
image_1_2_transformed = image_1_2.transform((640, 480),
                                            Image.Transform.AFFINE,
                                            data=T_inv.flatten()[:6],
                                            resample=Image.NEAREST)

# Showing image_1_2_transformed in a window using Matplotlib
plt.subplot(122) # On the right
plt.imshow(np.asarray(image_1_2_transformed))

# Show the image
plt.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 1.3

# Read a file, image_1_3
image_1_3 = Image.open("../vco_images/student_images/building4.JPG")

# Set matplotlib figure size
plt.figure(figsize=(12,4))

# Show image_1_3 in a window using Matplotlib
plt.subplot(121) # On the left
plt.imshow(np.asarray(image_1_3))

# Calculate sin and cos of +10 degree
angle = 10
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))

# Translation matrix
T_translate = np.array([
    [1, 0, 1000],
    [0, 1, 1000],
    [0, 0,    1]])

# Rotation matrix
T_rotate = np.array([
    [cos, -sin, 0],
    [sin,  cos, 0],
    [  0,    0, 1]])

# Scale matrix
T_scale = np.array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 1]])

# Center original to image center
T_center = np.array([
    [1, 0,  -image_1_3.width/2],
    [0, 1, -image_1_3.height/2],
    [0, 0,                   1]])

# Create the inverse transform matrix (Image.transform uses the inverse)
T = T_translate @ T_rotate @ T_scale @ T_center
T_inv = np.linalg.inv(T)

# Aply T_inv matrix to image_1_3
image_1_3_transformed = image_1_3.transform((2000, 2000),
                                            Image.Transform.AFFINE,
                                            data=T_inv.flatten()[:6],
                                            resample=Image.NEAREST)

# Showing image_1_3_transformed in a window using Matplotlib
plt.subplot(122) # On the right
plt.imshow(np.asarray(image_1_3_transformed))

# Show the image
plt.show()

# end of file #
