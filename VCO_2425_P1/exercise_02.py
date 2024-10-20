"""
@file     exercise_01.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Image manipulation.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import matplotlib.pyplot as plt                  # matplotlib = Matplotlib
import numpy as np                               # numpy = NumPy
from PIL import Image                            # PIL = Pilllow
from useful import showImageInfo, RESET, HEADER  # type: ignore

# ---------------------------------------------------------------------------- #
# EXERCISE 2.1

# Reading a file, image_2_1 (color tif type)
image_2_1 = Image.open("../vco_images/student_images/comet.jpeg")

# Converting image to 'P' type with palette
image_2_1 = image_2_1.convert(mode="P", palette=Image.ADAPTIVE, colors=4)

# Showing image_2_1 in a window using Matplotlib
image_2_1_array = np.array(image_2_1) # Convert the image to a numpy array
imgplot = plt.imshow(image_2_1_array, cmap='rainbow', vmin=0, vmax=4)
plt.colorbar(imgplot)

# Show the image
plt.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 2.2

# Reading a file, image_2_2
image_2_2 = Image.open("../vco_images/various_images/235.jpg")

# Showing original image information
print( HEADER + "EXERCISE 2.2 (Original image_2_2) ->" + RESET)
showImageInfo(image_2_2)

# Converting color image to 'L' type
image_2_2_2 = image_2_2.convert(mode="L")

# Showing modified image information
print( HEADER + "EXERCISE 2.2 (image_2_2_2) ->" + RESET)
showImageInfo(image_2_2_2)

# Showing image_2_2 and image_2_2_2 in a window using Pillow
image_2_2.show()
image_2_2_2.show()

# ---------------------------------------------------------------------------- #
# EXERCISE 2.3

# Reading a file, image_2_3
image_2_3 = Image.open("../vco_images/student_images/AloeVera.jpg")

# Save images for each single channel of the source image
image_2_3_r = image_2_3.getchannel("R")
image_2_3_g = image_2_3.getchannel("G")
image_2_3_b = image_2_3.getchannel("B")

# Showing image_2_3_r, image_2_3_g and image_2_3_b in a window using Pillow
image_2_3_r.show()
image_2_3_g.show()
image_2_3_b.show()

# end of file #
