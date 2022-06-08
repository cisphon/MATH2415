import sympy as sy
import math
import numpy as np


# https://www.chegg.com/homework-help/questions-and-answers/find-sets-parametric-equations-symmetric-equations-line-passes-given-point-parallel-given--q39739596
# Find sets of parametric equations and symmetric equations of the line that passes through the given point and is parallel to the given vector or line. (For each line, write the direction numbers as integers.)
def q1():
    point = (-3, 5, 6)

    denominator = [3, -4, 1]
 
    x, y, z, t = sy.symbols('x y z t')

    eq1 = sy.Eq(x, point[0] + t * denominator[0])
    eq2 = sy.Eq(y, point[1] + t * denominator[1])
    eq3 = sy.Eq(z, point[2] + t * denominator[2])

    # print eqs as a string
    print(str(eq1))
    print(str(eq2))
    print(str(eq3))

    # print the solution
    print(sy.solve(eq1))
    print(sy.solve(eq2))
    print(sy.solve(eq3))

# Find sets of parametric equations and symmetric equations of the line that passes through the two points (if possible). (For each line, write the direction numbers as integers.)
def q2():
    p1 = (0, 0, 81)
    p2 = (18, 18, 0)

    # direction vector
    d = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]

    # get the greatest common denominator of the direction vector
    gcd = sy.gcd(d[0], sy.gcd(d[1], d[2]))

    # divide the direction vector by the greatest common denominator (direction numbers)
    dn = (d[0] / gcd, d[1] / gcd, d[2] / gcd)

    # (a) parametric
    print('x = ' + str(p1[0]) + '+' + str(dn[0]) + 't\n' + 'y = ' + str(p1[1]) + '+' + str(dn[1]) + 't\n' + 'z = ' + str(p1[2]) + '+' + str(dn[2]) + 't')

    # (b) symmetric
    print('(x' + '-' + str(p1[0]) + ') / ' + str(dn[0]) + ' = (y' + '-' + str(p1[1]) + ') / ' + str(dn[1]) + ' = (z' + '-' + str(p1[2]) + ') / ' + str(dn[2]))

# Find a set of parametric equations of the line with the given characteristics. (Use t for the parameter. Enter your answers as a comma-separated list of equations.)
def q3():
    p = (-5, 7, 9)

    dn = [-1, 5, 1]

    # parametric
    print('x = ' + str(p[0]) + '+' + str(dn[0]) + 't\n' + 'y = ' + str(p[1]) + '+' + str(dn[1]) + 't\n' + 'z = ' + str(p[2]) + '+' + str(dn[2]) + 't')

# Find the coordinates of a point P on the line and a vector v parallel to the line.
def q4():
    # make the numerators equal 0 (x-2, y+3, z+8) (solve for x-2 = 0 and y + 3 = 0 and z + 8 = 0) and you'll get p
    p = (1, -5, -9)
    print(p)

    # denominator
    v = [5, 8, 1]
    print(v)

# Determine whether the lines are parallel or identical.
def q5():
    x, y, z, t = sy.symbols('x y z t')

    eq_x_1 = sy.Eq(x, 6 - 3 * t)
    eq_x_2 = sy.Eq(x, 6 * t)

    eq_y_1 = sy.Eq(y, -2 + 2 * t)
    eq_y_2 = sy.Eq(y, 2 - 4 * t)

    eq_z_1 = sy.Eq(z, 4 + 4 * t)
    eq_z_2 = sy.Eq(z, 12 - 8 * t)

    # check if the equations are parallel
    if sy.solve(eq_x_1) == sy.solve(eq_x_2) and sy.solve(eq_y_1) == sy.solve(eq_y_2) and sy.solve(eq_z_1) == sy.solve(eq_z_2):
        print('The lines are parallel.')
    else:
        print('The lines are identical.')
    


# Find an equation of the plane that passes through the given point and is perpendicular to the given vector or line.
def q7():
    p = (2, 4, -5)

    # perpendicular to n = j
    v = [0, 1, 0] # j is 1 

    # in this case, the solution is y - 3 = 0
    print(str(v[0]) + '(x-' + str(p[0]) + ') + ' + str(v[1]) + '(y-' + str(p[1]) + ') + ' + str(v[2]) + '(z-' + str(p[2]) + ') = 0')

# UNFINISHED
# Find an equation of the plane with the given characteristics.
def q8():
    # The plane contains the y-axis and makes an angle of 𝜋/2 with the positive x-axis.
    p1 = (0, 0, 0)
    p2 = (0, 1, 0)
    p3 = (1, 0, math.sqrt(2))

    # u is from p1 to p2
    u = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]

    # v is from p1 to p3
    v = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]

    # w is the cross product of u and v
    w = np.cross(u, v)

    print(w)


if __name__ == "__main__":
    q5()
