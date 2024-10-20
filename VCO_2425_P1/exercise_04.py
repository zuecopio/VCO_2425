"""
@file     exercise_04.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    3D visualization.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import matplotlib.pyplot as plt  # matplotlib = Matplotlib
import numpy as np               # numpy = NumPy
from PIL import Image            # PIL = Pilllow

# ---------------------------------------------------------------------------- #
# EXERCISE 4.1

# Reading a file, image_4_1 (grayscale type)
image_4_1 = Image.open('../vco_images/student_images/cameraman.tif')

# Convert the image to a numpy array
data = np.array(image_4_1)

# Create a value grid for the surface
x = np.linspace(start=0, stop=data.shape[0] - 1, num=data.shape[0])
y = np.linspace(start=0, stop=data.shape[1] - 1, num=data.shape[1])
X, Y = np.meshgrid(x,y)

# Create the contour plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
plt.contourf(X, Y, data, levels=100, cmap='gray')

# Adjust aspect ratio
ax.set_box_aspect([1, 1, 0.2])
ax.set_zticks(np.arange(0, 255, 100))  # Intervals of 100 for the z axis

# Invert the Y axis so that the image displays correctly
plt.gca().invert_yaxis()

# Show image as surface
plt.show()

# end of file #
