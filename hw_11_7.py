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

# Find an equation in rectangular coordinates for the surface represented by the cylindrical equation.
def q4():
    theta = math.pi / 3
    
    tan_theta = 'just look what tan(π/3) is'

    # tan_theta = y / x

    # solve for x
    # then move y to the left side and make it equal to 0


# Find an equation in rectangular coordinates for the surface represented by the cylindrical equation.
def q5():
    # just replace r^2 with x^2 + y^2

    # r^2 + z^2 = 4
    print('x^2 + y^2 + z^2 = 4')

# Find an equation in rectangular coordinates for the surface represented by the cylindrical equation.
def q6():
    # r = 5 cos(theta)
    # r^2 = 5rcos(theta) // multiply both sides by r
    # x^2 + y^2 = 5x // replace r^2 with x^2 + y^2 and rcos(theta) with x
    # x^2 + y^2 - 5x = 0 // move 5x to the left side

    # the graph looks like it goes from 0 to 5 (off center)
    pass

# Convert the point from rectangular coordinates to spherical coordinates.
def q7():
    # p = sqrt(x^2 + y^2 + z^2)
    # theta = arctan(y/x)
    # phi = arccos(z/p)

    # use wolfram alpha for theta

    x, y, z = -1, 2, 1

    r = x**2 + y**2 + z**2 # this is technically p
    numerator = z
    denominator = (x**2 + y**2 + z**2)

    print('sqrt(' + str(r) + ')', 'wolfram solution', 'arccos(sqrt(' + str(numerator**2) + ')/sqrt(' + str(denominator) + '))')

# Convert the point from spherical coordinates to rectangular coordinates.
def q8():
    # x = p sin(phi) cos(theta)
    # y = p sin(phi) sin(theta)
    # z = p cos(phi)

    p = 6
    phi = math.pi / 4
    theta = math.pi / 6

    x = p * math.sin(phi) * math.cos(theta)
    y = p * math.sin(phi) * math.sin(theta)
    z = p * math.cos(phi)

    # use wolfram alpha for this. lol
    # https://www.wolframalpha.com/input?i=6+*+sin%28pi%2F4%29+*+cos%28pi%2F6%29

    
# Find an equation in spherical coordinates for the surface represented by the rectangular equation.
def q9():
    # given x^2 + y^2 + z^2 - 7z = 0
    # p^2 - 7p cos(phi) = 0
    # p^2 = 7p cos(phi) // moved 7pcos(phi) to the right side
    # p = 7cos(phi) // divided both sides by p
    print('BE SURE TO USE THE p SYMBOL INSTEAD OF TYPING P')

# Find an equation in rectangular coordinates for the surface represented by the spherical equation.
# theta = pi / 4
def q10():
    # https://www.chegg.com/homework-help/questions-and-answers/find-equation-rectangular-coordinates-surface-represented-spherical-equation-4-sketch-grap-q29913869
    pass
 
# Find an equation in rectangular coordinates for the surface represented by the spherical equation.
# 7 csc(phi)sec(theta) = p
# solution is x = 7
def q11():
    # https://www.chegg.com/homework-help/questions-and-answers/find-equation-rectangular-coordinates-surface-represented-spherical-equation-9-csc-sec-q34905304
    pass

# Convert the point from cylindrical coordinates to spherical coordinates.
# THIS ONE NEEDS TO BE FIXED
def q12():
    # use wolfram alpha for this. lol
    # and use this below
    # https://math.wvu.edu/~hlai2/Teaching/Tip-Pdf/Tip3-21.pdf

    # r = -4
    # theta = math.pi / 3
    # z = 4

    # x = r cos(theta) = -2
    # y = r sin(theta) = -2sqrt(3)
    # z = z = 4

    # p = sqrt((rcos(theta))^2 + (rsin(theta)^2 + z^2)) = 4sqrt(2) 
    # theta = arctan(rsin(theta) / rcos(theta)) = pi/3
    # phi = arctan((sqrt(rcos(theta)^2 + rsin(theta)^2)) / z) = pi/4
    pass


# Convert the point from spherical coordinates to cylindrical coordinates. (Choose r > 0 and −2𝜋 ≤ 𝜃 < 0).
def q13():
    # (p, theta, phi) -> (x, y, z) -> (r, theta, z)

    # use wolfram alpha for this. lol
    # and use this below
    # https://math.wvu.edu/~hlai2/Teaching/Tip-Pdf/Tip3-21.pdf

    # p = 4
    # theta = - pi / 6
    # phi = pi / 3

    # x = p sin(phi) cos(theta) = 3
    # y = p sin(phi) sin(theta) = -sqrt(3)
    # z = p cos(phi) = 2

    # r = sqrt(x^2 + y^2) = 2 sqrt(3)
    # theta = arctan(y/x) =  - pi / 6
    # z = z = 2

    pass


    

    
# Convert the rectangular equation to an equation in cylindrical coordinates and spherical coordinates.
def q14():

    # useful info.
    # https://math.wvu.edu/~hlai2/Teaching/Tip-Pdf/Tip3-21.pdf

    pass
    


if __name__ == "__main__":
    q12()

