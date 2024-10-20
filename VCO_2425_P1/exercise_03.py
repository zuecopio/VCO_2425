"""
@file     exercise_03.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Arithmetic with images.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import matplotlib.pyplot as plt                  # matplotlib = Matplotlib
from useful import showImageInfo, RESET, HEADER  # type: ignore
import numpy as np                               # numpy = NumPy
from PIL import Image                            # PIL = Pilllow

# ---------------------------------------------------------------------------- #
# EXERCISE 3.1

# Reading a file, image_3_1
image_3_1 = Image.open("../vco_images/student_images/cameraman.tif")

# Showing image information
print( HEADER + "EXERCISE 3.1 (image_3_1) ->" + RESET)
showImageInfo(image_3_1)

# Showing image_3_1 in a window using Pillow
image_3_1.show()

# Reading a file, image_3_1_2
image_3_1_2 = Image.open("../vco_images/student_images/moon.tif")

# Showing image information
print( HEADER + "EXERCISE 3.1 (image_3_1_2) ->" + RESET)
showImageInfo(image_3_1_2)

# Showing image_3_1_2 in a window using Pillow
image_3_1_2.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 3.2

# Resize image_3_1 and image_3_1_2 images to 230x230
image_3_2 = image_3_1.resize((230, 230))
image_3_2_2 = image_3_1_2.resize((230, 230))

# Showing images information
print( HEADER + "EXERCISE 3.2 (image_3_2) ->" + RESET)
showImageInfo(image_3_2)
print( HEADER + "EXERCISE 3.2 (image_3_2_2) ->" + RESET)
showImageInfo(image_3_2_2)

# Showing image_3_1 in a window using Pillow
image_3_2.show()
image_3_2_2.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 3.3

# Convert image_3_2 and image_3_2_2 to a numpy array
image_3_2_array = np.array(image_3_2)
image_3_2_2_array = np.array(image_3_2_2)

# Applying some arithmetic operations
image_3_3_array = (image_3_2_array) + (image_3_2_2_array)

# Showing image_3_3_array in a window using Matplotlib
imgplot = plt.imshow(image_3_3_array, cmap='gray_r', vmin=0, vmax=255)
plt.colorbar(imgplot)

# Show the image
plt.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 3.4

# Applying linear equation: [ S = IMG1 * 1.8 - IMG2 * 1.2 + 128 ]
image_3_4_array = (image_3_2_array * 1.8) - ((image_3_2_2_array * 1.2) + 128.0)

# Showing image_3_4_array in a window using Matplotlib
imgplot = plt.imshow(image_3_4_array, cmap='gray_r', vmin=0, vmax=255)
plt.colorbar(imgplot)

# Show the image
plt.show()

# end of file #
