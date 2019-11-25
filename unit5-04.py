#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program calculates the volume of a cylinder

import math


def volume(radius_input, height_input):
    # Process
    if radius_input <= 0 or height_input <= 0:
        area = -1
        return area
    else:
        area = math.pi * (radius_input ** 2) * height_input
        return area


def main():
    # This function gets the input and calls another function

    # Input
    radius = input("Please enter the radius (cm): ")
    height = input("Please enter the height (cm): ")
    try:
        radius = int(radius)
        height = int(height)
    except(Exception):
        print("Invalid input!!!")
        return

    # pass the variables to the function and get the result
    result = volume(radius, height)

    # Output
    if result == -1:
        print("The input must be more than 0!")
    else:
        print("The area of the cylinder is {0:.2f} cm^3".format(result))


if __name__ == "__main__":
    main()
