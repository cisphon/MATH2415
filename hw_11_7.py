import math
import numpy as np
from fractions import Fraction

# Convert the point from cylindrical coordinates to rectangular coordinates.
def q1():
    r, theta, z = 2, np.deg2rad(0), -7

    x = Fraction(r * math.cos(theta)).limit_denominator(20)
    y = Fraction(r * math.sin(theta)).limit_denominator(20)

    print(x, y, z)

# Convert the point from rectangular coordinates to cylindrical coordinates.
def q2():
    x, y, z = 6, 2 * math.sqrt(3), -9
    
    r = x**2 + y**2 # needs to be squared later

    # put theta in degrees
    theta = Fraction(np.arctan(y/x) / math.pi).limit_denominator(10)

    print('sqrt(' + str(r) + ')', 'π*' + str(theta), z)

# Find an equation in cylindrical coordinates for the surface represented by the rectangular equation.
def q3():
    # just replace x^2 + y^2 with r^2
    # x^2 + y^2 + z^2 - 6z = 0
    print('r^2 + z^2 - 6z = 0')

def q4():
    theta = math.pi / 3


if __name__ == "__main__":
    q1()

