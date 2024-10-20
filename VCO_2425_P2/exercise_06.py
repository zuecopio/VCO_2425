"""
@file     exercise_06.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Perspective rectification of an image.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import cv2
import numpy as np  
from utils import ginput # type: ignore

# ---------------------------------------------------------------------------- #
# EXERCISE 6.1

# Read a file, image_6_1
image_6_1 = cv2.imread("../vco_images/student_images/Santa-Maria-Micaela-2.jpg")

# Show image_6_1 in a window using OpenCV
cv2.imshow("Select 4 points", image_6_1)

# Graphic input of 4 points
points = ginput("Select 4 points", image_6_1, 5)

print("Selected points: ")
print(points)

outs = [[0,0], [200,0], [200,200], [0,200]] + points[0]
outs = np.array(outs,np.float32)

print("Points with the corresponding geometric transformation: ")
print(outs)

# Obtener la matriz de transformación de perspectiva
T = cv2.getPerspectiveTransform(points,outs)

# ---------------------------------------------------------------------------- #
# EXERCISE 6.2

# Get the dimensions of the image
height, width = image_6_1.shape[:2]

# Aply T matrix to image_6_1
image_6_1_transformed = cv2.warpPerspective(image_6_1, T, (width, height))

# ---------------------------------------------------------------------------- #
# EXERCISE 6.3

# Show image_6_1_transformed in a window using OpenCV
cv2.imshow("Rectified image", image_6_1_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------------------------------------------------------------- #
# EXERCISE 6.4

# Read a file, image_6_4
image_6_4 = cv2.imread("../vco_images/student_images/building4-1.JPG")

# Show image_6_4 in a window using OpenCV
cv2.imshow("Select 4 points", image_6_4)

# Graphic input of 4 points
points = ginput("Select 4 points", image_6_4, 5)

print("Selected points: ")
print(points)

outs = [[0,0], [200,0], [200,200], [0,200]] + points[0]
outs = np.array(outs,np.float32)

print("Points with the corresponding geometric transformation: ")
print(outs)

# Obtener la matriz de transformación de perspectiva
T = cv2.getPerspectiveTransform(points,outs)

# Get the dimensions of the image
height, width = image_6_4.shape[:2]

# Aply T matrix to image_6_4
image_6_4_transformed = cv2.warpPerspective(image_6_4, T, (width, height))

# Show image_6_4_transformed in a window using OpenCV
cv2.imshow("Rectified image", image_6_4_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()

# end of file #
