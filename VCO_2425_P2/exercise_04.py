"""
@file     exercise_04.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    OpenCV visualization using Matplotlib.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import cv2
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------- #
# EXERCISE 4

src = cv2.imread("../vco_images/student_images/building4.JPG")
dst = cv2.resize(src, (256, 256), interpolation=cv2.INTER_CUBIC)

# Set matplotlib figure size
plt.figure(figsize=(12,4))

# Showing src and dst in a window using Matplotlib
plt.subplot(121),plt.imshow(src),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')

# Show the image
plt.show()

# end of file #
