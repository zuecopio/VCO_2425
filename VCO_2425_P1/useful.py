"""
@file     useful.py

@author   Marcos Belda Martinez <mbelmar@etsinf.upv.es>
@date     October, 2024
@section  VCO-GIIROB
@brief    Some defines and functions to use in exercises.
"""

# ---------------------------------------------------------------------------- #
# NEEDED IMPORTS

from PIL import Image # PIL = Pilllow

# ---------------------------------------------------------------------------- #
# COLOR DEFINES

PURPLE = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"
HEADER = BOLD + PURPLE

# ---------------------------------------------------------------------------- #
# USEFUL FUNCTIONS

def showImageInfo(image):
    """
    This function displays information such as the format,
    size, mode, and number of colors of a PIL Image.
    """
    imageInfo  = BOLD + "    Format: " + RESET + str(image.format) + "\n"
    imageInfo += BOLD + "    Size: "   + RESET + str(image.size)   + "\n"
    imageInfo += BOLD + "    Mode: "   + RESET + str(image.mode)   + "\n"

    if image.mode != 'P':
        image = image.convert(mode="P")

    colores = image.getcolors()
    num_colores = len(colores)
    imageInfo += BOLD + "    Num. of colors: " + RESET + str(num_colores) + "\n"

    print(imageInfo)

    ### end def showImageInfo() ###

# end of file #
