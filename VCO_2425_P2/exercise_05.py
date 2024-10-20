"""
@file     exercise_05.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Combining image transformations with OvenCV.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import cv2
import math
import numpy as np  

# ---------------------------------------------------------------------------- #
# EXERCISE 5.1

# Read a file, image_5_1
image_5_1 = cv2.imread("../vco_images/student_images/building4.JPG")

# Show image_5_1 in a window using OpenCV
cv2.imshow("Imagen original", image_5_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------- #
# EXERCISE 5.2

# Read a file, image_5_2
image_5_2 = cv2.imread("../vco_images/student_images/building4.JPG")

# -10 degree (Counter-clockwise rotation)
angle = -10

# Rotation matrix
M_rotate = cv2.getRotationMatrix2D((0, 0), angle, 1)

# Aply M_inv matrix to image_5_2
image_5_2_transformed = cv2.warpAffine(image_5_2, M_rotate, (640, 480))

# Show image_5_2 and image_5_2_transformed in a window using OpenCV
cv2.imshow("Original image", image_5_2)
cv2.imshow("Rotated image", image_5_2_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------- #
# EXERCISE 5.3

# Read a file, image_5_3
image_5_3 = cv2.imread("../vco_images/student_images/building4.JPG")

# Get the dimensions of the image
height, width = image_5_3.shape[:2]
center_x = width / 2
center_y = height / 2

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
    [1, 0, -center_x],
    [0, 1, -center_y],
    [0, 0,        1]])

# Create the transform matrix
T = T_translate @ T_rotate @ T_scale @ T_center

# Aply T matrix to image_5_3
image_1_3_transformed = cv2.warpPerspective(image_5_3, T, (2000, 2000))

# Show image_5_3 and image_5_3_transformed in a window using OpenCV
cv2.imshow("Original image", image_5_3)
cv2.imshow("Rotated image", image_1_3_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# end of file #
