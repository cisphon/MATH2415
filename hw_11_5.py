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
    
# Determine whether the lines intersect, and if so, find the point of intersection. (If an answer does not exist, enter DNE.)
def q6():
    # x = 8t + 2,    y = 7,    z = −t + 1
    # x = 2s + 2,    y = 2s + 7,    z = s + 1

    # The vectors u and v are based on the coefficient of t and s.
    u = [8, 0, -1]
    v = [2, 2, 1]

    # substitute zero into t and s in the equations above. (the addition and subtraction remains)
    print(2, 7, 1)


    cos_theta = np.abs(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)))

    # in degrees, rounded to the nearest tenth
    print(round(math.degrees(math.acos(cos_theta)), 1))




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

# Determine whether the planes are parallel or identical.
# −7x + 5y − 9z = 4
# 14x − 10y + 18z = 7
def q9():
    x, y, z = sy.symbols('x y z')

    eq_1 = sy.Eq(4, -7*x+5*y-9*z)
    eq_2 = sy.Eq(7, 14*x-10*y+18*z)

    # these equations are parallel but they are not identical because the intersection is not the same
    print(sy.solve(eq_1))
    print(sy.solve(eq_2))

# Consider the following planes.
# −3x + y + z	 = 	3
# 18x − 6y + 3z	 = 	9
def q10():
    u = [-5, 1, 1]
    v = [20, -4, 5]

    # u = 5
    # v = 25
    w = [5, 25]

    # find the angle between the two planes (round your answer to two decimal places)
    cos_theta = np.abs(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)))
    print(round(math.degrees(math.acos(cos_theta)), 2))


    # Find a set of parametric equations for the line of intersection of the planes. (Use t for the parameter. Enter your answers as a comma-separated list of equations.)

    # consider z = t
    intersection = np.cross(u, v)

    x, y, z, t = sy.symbols('x y z t')

    eq_1 = sy.Eq(w[0], u[0]*x + u[1]*y + u[2]*z)
    eq_2 = sy.Eq(w[1], v[0]*x + v[1]*y + v[2]*z)


    thing = list(sy.linsolve([eq_1, eq_2], [x, y, z]))[0]

    print(thing)

    print("if there is a constant by itself, then it's place (x, y, z) is that value.")
    print("in your case, it is %s (subject to change)" % thing[0])

    x_var = thing[0]

    print(x)

# Consider the following.
def q11():
    x, y, z = sy.symbols('x y z')

    eq = sy.Eq(2 * x - y + z, 6)

    # substitute y and z for 0. (x intercept)
    x_intercept = sy.solve(eq.subs(y, 0).subs(z, 0), x)[0]
    print(str(x_intercept) + ' 0 0')

    # substitute x and z for 0. (y intercept)
    y_intercept = sy.solve(eq.subs(x, 0).subs(z, 0), y)[0]
    print('0 ' + str(y_intercept) + ' 0')

    # substitute x and y for 0. (z intercept)
    z_intercept = sy.solve(eq.subs(x, 0).subs(y, 0), z)[0]
    print('0 0 ' + str(z_intercept))


# Find the distance between the point and the plane.
def q12():
    Q = (0,0,0)

    # 3x + 6y + z = 18
    plane = [3, 6, 1, 18]

    # normal to plane
    n = [plane[0], plane[1], plane[2]]

    x, y, z = sy.symbols('x y z')

    # find the point of intersection
    p = sy.solve(sy.Eq(plane[0]*x + plane[1]*y + plane[2]*z, plane[3]), [x, y, z])[0]

    a = p[0].subs(y, 0).subs(z, 0)
    b = p[1].subs(y, 0)
    c = p[2].subs(z, 0)

    PQ = [a, b, c]

    numerator = abs(np.dot(PQ, n))
    denominator = np.linalg.norm(n) ** 2
    D = numerator / denominator

    print(str(numerator) + "/ sqrt(" + str(denominator) + ")")

# Verify that the two planes are parallel.
# if all else fails, use this: https://onlinemschool.com/math/assistance/cartesian_coordinate/plane_plane/
def q13():

    # if you get weird results then swap v and u, also check the next comment
    v = [-1, 6, 2]
    u = [-1/2, 3, 1]

    # swap these numbers too.
    w = [7, 8]
    '''

    u = [2, -3, 1]
    v = [4, -6, 2]

    w = [4, 3]
    '''

    print(u)
    print(v)

    # if they're all the same, then they're u and v are parallel
    # make sure that n1 = C * n2
    for i in range(len(u)):
        print(u[i] / v[i], end=' ')
    print()

    # find the distance between the two planes

    a = v[0]
    b = v[1]
    c = v[2]
    d = -w[1]

    print(a, b, c, d)
    
    x, y, z = sy.symbols('x y z')

    eq = sy.Eq(u[0]*x + u[1]*y + u[2]*z + -w[0], 0)

    # solve for x when y = 0 and z = 0
    x_intercept = sy.solve(eq.subs(y, 0).subs(z, 0), x)[0]
    y_intercept = 0
    z_intercept = 0

    print(x_intercept, y_intercept, z_intercept)

    numerator = abs(a*x_intercept + b*y_intercept + c*z_intercept + d)
    denominator = a**2 + b**2 + c**2

    print(str(numerator) + "/ sqrt(" + str(denominator) + ")")


    

# Find the distance between the point and the line given by the set of parametric equations. (Round your answer to three decimal places.)
# (9, -8, 1); x = 2t, y = t − 3, z = 2t + 2
def q14():
    # the coefficients of the variables in the equation
    # x = 2t, y = t - 3, z = 2t + 2

    Q = (9, -8, 1)

    # based upon the coefficients of x, y, and z
    u = [2, 1, 2]


    x, y, z, t = sy.symbols('x y z t')

    # lambda function to store into 3 points
    f = lambda t: [2*t, t - 3, 2*t + 2]
    P = f(0)

    PQ = [Q[0] - P[0], Q[1] - P[1], Q[2] - P[2]]

    PQ_x_u = np.cross(PQ, u)

    # normalize PQ_x_u
    PQ_x_u_norm = np.linalg.norm(PQ_x_u)

    # normalize u
    u_norm = np.linalg.norm(u)

    # round to 3 decimal places of PQ_x_u_norm / u_norm
    print(round(PQ_x_u_norm / u_norm, 3))


    
# https://www.chegg.com/homework-help/questions-and-answers/figure-shows-chute-top-grain-elevator-combine-funnels-grain-bin-find-angle-two-adjacent-si-q66982998
# The figure shows a chute at the top of a grain elevator of a combine that funnels the grain into a bin. Find the angle between two adjacent sides. (Round your answer to one decimal place.)
def q15():
    print("I don't know how he/she got (-1, -1, 8)")


if __name__ == "__main__":
    q13()
