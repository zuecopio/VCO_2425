"""
@file     exercise_03.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Point transformations.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

import math
import matplotlib.pyplot as plt
import numpy as np  
import string

# ---------------------------------------------------------------------------- #
# EXERCISE 3

# Define coordinates of the points (homogeneous coordinates)
a = ( 0,  1, 1)
b = ( 1,  0, 1)
c = ( 0, -1, 1)
d = (-1,  0, 1)

# Create a numpy array with the points
A = np.array([a, b, c, d])

# Calculate sin and cos of -30 degree
angle = -30
sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))

# Translation matrix
T_translate = np.array([
    [1, 0, -3],
    [0, 1,  3],
    [0, 0,  1]])

# Scale matrix
T_scale = np.array([
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 1]])

# Rotation matrix
T_rotate = np.array([
    [cos, -sin, 0],
    [sin,  cos, 0],
    [  0,    0, 1]])

# Create the transform matrix
T = T_translate @ T_scale @ T_rotate

# 3x3 Identity transformation matrix
I = np.eye(3)

# Define a string containing color codes
color_lut = 'rgbc'

fig  = plt.figure()  # Create a new figure for plotting.
ax   = plt.gca()     # Get the current axes of the figure.

xs_s = []  # Initialize an empty list to store transformed x-coordinates
ys_s = []  # Initialize an empty list to store transformed y-coordinates
i    = 0   # Initialize an index variable for tracking the current row

# Iterate over each row in the matrix A
for row in A:
    output_row = T @ row  # Multiply the transformation matrix T
    x, y, h = row
    x_s, y_s, k = output_row
    
    xs_s.append(x_s) # Append the transformed x-coordinate to the xs_s list
    ys_s.append(y_s) # Append the transformed y-coordinate to the xy_s list

    c = color_lut[i] # Assign a color

    # Create scatter plots for the original and transformed points
    plt.scatter(x, y, color=c)
    plt.scatter(x_s, y_s, color=c)

    # Add text annotations (ASCII letters) for the original and transformed points
    plt.text(x + 0.15, y, f"{string.ascii_letters[int(i)]}")
    plt.text(x_s + 0.15, y_s, f"{string.ascii_letters[int(i)]}'")

    i += 1  # Increment the index for the next iteration

# Close the loop by appending the first transformed x and y coordinates
xs_s.append(xs_s[0])
ys_s.append(ys_s[0])

# Plot dotted lines connecting the transformed points and the original points
plt.plot(x_s, y_s, color="gray", linestyle='dotted')
plt.plot(xs_s, ys_s, color="gray", linestyle='dotted')

# Set the x-ticks and y-ticks of the axes with specified ranges and steps
ax.set_xticks(np.arange(start=-6, stop=3, step=1.0))
ax.set_yticks(np.arange(start=-2, stop=7, step=1.0))

# Add a grid to the window
plt.grid()

# Show the points
plt.show()

# end of file #
