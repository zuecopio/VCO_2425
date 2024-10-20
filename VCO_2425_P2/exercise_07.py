"""
@file     exercise_07.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Color space transformation.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import cv2
from utils import ginput # type: ignore

# ---------------------------------------------------------------------------- #
# EXERCISE 7.1

# Read a file, image_7_1
image_7_1 = cv2.imread("../vco_images/student_images/AloeVera_02.jpg")

# Separate the color channels (B, G, R)
B, G, R = cv2.split(image_7_1)

# Show the three channels separately (gray images)
cv2.imshow('Blue', B)
cv2.imshow('Green', G)
cv2.imshow('Red', R)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------- #
# EXERCISE 7.2

# Read a file, image_7_2
image_7_2 = cv2.imread("../vco_images/student_images/AloeVera_02.jpg")

# Convert from RGB to HSV
image_7_2_hsv = cv2.cvtColor(image_7_2, cv2.COLOR_BGR2HSV)

# Separate the channels (H, S, V)
H, S, V = cv2.split(image_7_2_hsv)

# Show the three channels separately (gray images)
cv2.imshow('Hue', H)
cv2.imshow('Saturation', S)
cv2.imshow('Value', V)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------- #
# EXERCISE 7.3

# Read a file, image_7_3
image_7_3 = cv2.imread("../vco_images/student_images/AloeVera_02.jpg")

# Convert from RGB to HSV
image_7_3_lab = cv2.cvtColor(image_7_3, cv2.COLOR_BGR2LAB)

# Separate the channels (H, S, V)
L, A, B = cv2.split(image_7_3_lab)

# Show the three channels separately (gray images)
cv2.imshow('Lightness', L)
cv2.imshow('Green to Red', A)
cv2.imshow('Blue to Yellow', B)

cv2.waitKey(0)
cv2.destroyAllWindows()

# end of file #
