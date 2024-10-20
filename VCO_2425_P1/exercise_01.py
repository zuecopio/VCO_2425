"""
@file     exercise_01.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Working with images.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import matplotlib.pyplot as plt                  # matplotlib = Matplotlib
import numpy as np                               # numpy = NumPy
from PIL import Image                            # PIL = Pilllow
from useful import showImageInfo, RESET, HEADER  # type: ignore

# ---------------------------------------------------------------------------- #
# EXERCISE 1.1

# Reading a file, image_1_1
image_1_1 = Image.open("../vco_images/various_images/235.jpg")

# Showing image information
print( HEADER + "EXERCISE 1.1 (image_1_1) ->" + RESET)
showImageInfo(image_1_1)

# Showing image_1_1 in a window using Pillow
image_1_1.show()

# Reading a file, image_1_1_2
image_1_1_2 = Image.open("../vco_images/student_images/comet.jpeg")

# Showing image information
print( HEADER + "EXERCISE 1.1 (image_1_1_2) ->" + RESET)
showImageInfo(image_1_1_2)

# Showing image_1_1_2 in a window using Pillow
image_1_1_2.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 1.2

# Reading a file, image_1_2 (color tif type)
image_1_2 = Image.open("../vco_images/license_plates/M9205OB.tif")

# Showing image information
print( HEADER + "EXERCISE 1.2 (image_1_2) ->" + RESET)
showImageInfo(image_1_2)

# Showing image_1_2 in a window using Matplotlib
image_1_2_array = np.array(image_1_2) # Convert the image to a numpy array
imgplot = plt.imshow(image_1_2_array, cmap='gray', vmin=0, vmax=255)
plt.colorbar(imgplot)

# Show the image
plt.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 1.3

# Reducing the number of colors of the last image (image_1_2)
image_1_3 = image_1_2.quantize(colors=16)

# Showing image information
print( HEADER + "EXERCISE 1.3 (image_1_2) ->" + RESET)
showImageInfo(image_1_2)
print( HEADER + "EXERCISE 1.3 (image_1_3) ->" + RESET)
showImageInfo(image_1_3)

# Showing image_1_2 and image_1_3 in a window using Pillow
image_1_2.show()
image_1_3.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 1.4

# Reading a file, image_1_4
image_1_4 = Image.open("../vco_images/various_images/m40.jpg")

# Showing original image information
print( HEADER + "EXERCISE 1.4 (Original image_1_4) ->" + RESET)
showImageInfo(image_1_4)

# Converting image to 'P' type with palette
image_1_4 = image_1_4.convert(mode="P", dither=1, palette=Image.ADAPTIVE)

# Showing image_1_4 in a window using Matplotlib
image_1_4_array = np.array(image_1_4) # Convert the image to a numpy array
imgplot = plt.imshow(image_1_4_array, cmap='autumn_r', vmin=0, vmax=255)
plt.colorbar(imgplot)

# Show the image
plt.show()

# Reducing the number of colors of image_1_4
image_1_4_2 = image_1_4.quantize(colors=16)

# Showing image information
print( HEADER + "EXERCISE 1.3 (image_1_4_2) ->" + RESET)
showImageInfo(image_1_4_2)

# Showing image_1_4 and image_1_4_2 in a window using Pillow
image_1_4.show()
image_1_4_2.show()

# end of file #
