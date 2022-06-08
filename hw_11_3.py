import numpy as np
import sympy as sy
from scipy.linalg import qr
from fractions import Fraction

# dot product of two vectors


def q1():
    u = [4, -2, 5]
    v = [0, 7, 5]

    # u dot v
    print(np.dot(u, v))

    # u dot u
    print(np.dot(u, u))


    # magnitude of v squared
    print(np.linalg.norm(v) ** 2)

    # (u dot v) dot v
    print(np.dot(np.dot(u, v), v))

    # u dot (3 times v)
    print(np.dot(u, np.dot(3, v)))

# Find the angle theta between the vectors in radians and in degress.
def q2():
    u = [6, 3, 1]
    v = [3, -6, 0]

    # theta in radians
    print(np.arccos(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))))

    # theta in degrees
    print(np.arccos(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))) * (180 / np.pi))

# use the alternative form of the dot product to find u.v
def q3():
    # u.v = |u| |v| cos(theta)
    mag_u = 25
    mag_v = 50
    theta = sy.pi * 5.0 / 6.0 # just for reference, too lazy to make this program better.

    print(mag_u * mag_v, ' cos(', sy.pi, ' * 5 / 6) = ')

# Determine whether u and v are orthogonal, parallel, or neither.
def q4():
    u = [0, 1, 9]
    v = [1, -5, -1]

    # check if u and v are orthogonal
    if np.dot(u, v) == 0:
        print('u and v are orthogonal')
    # check if u and v are parallel
    elif np.dot(u, v) == np.linalg.norm(u) * np.linalg.norm(v):
        print('u and v are parallel')
    else:
        print('neither')



# The vertices of a triangle are given. Determine whether the triangle is an acute triangle, an obtuse triangle, or a right triangle.
def q5():
    a = np.array([-9, 0, 0])
    b = np.array([0, 0, 0])
    c = np.array([7, 2, 6])

    u = a - b
    v = a - c
    w = b - c

    mag_u = np.linalg.norm(u)
    mag_v = np.linalg.norm(v)
    mag_w = np.linalg.norm(w)


    # the angle between u and v is
    angle_u_v = np.degrees(np.arccos(np.dot(u, v) / (mag_u * mag_v)))

    # the angle between v and w is
    angle_v_w = np.degrees(np.arccos(np.dot(v, w) / (mag_v * mag_w)))

    # the angle between u and w is
    last_angle = 180 - angle_u_v - angle_v_w

    # check if the triangle is a right triangle
    if angle_u_v == 90 or angle_v_w == 90 or last_angle == 90:
        print('right triangle')
    # check if the triangle is an acute triangle
    elif angle_u_v < 90 and angle_v_w < 90 and last_angle < 90:
        print('acute triangle')
    # check if the triangle is an obtuse triangle
    elif angle_u_v > 90 or angle_v_w > 90 or last_angle > 90:
        print('obtuse triangle')

# Find the direction cosines and angles of u and show that cos2 𝛼 + cos2 𝛽 + cos2 𝛾 = 1.
# (Round your answers for the angles to four decimal places.)
def q6():
    u = [1, 4, 8]

    u_mag = np.linalg.norm(u)

    cos_a = u[0] / u_mag
    print(u[0], ' / ', u_mag, ' = ', round(cos_a, 4))
    cos_b = u[1] / u_mag
    print(u[1], ' / ', u_mag, ' = ', round(cos_b, 4))
    cos_y = u[2] / u_mag
    print(u[2], ' / ', u_mag, ' = ', round(cos_y, 4))


    a = np.arccos(cos_a)
    print('a = ', round(a, 4))
    b = np.arccos(cos_b)
    print('b = ', round(b, 4))
    y = np.arccos(cos_y)
    print('y = ', round(y, 4))



# Consider the following.
# BE SURE TO PUT A VECTOR INSTEAD OF I + J
def q7():
    u = np.array([5, 2])
    v = np.array([8, 6])

    numerator = np.dot(np.dot(u, v), v)
    denominator = np.linalg.norm(v) ** 2


    proj_u_on_v = []
    print('Projection of u onto v: ')
    for i in numerator:
        fraction = Fraction((i / denominator)).limit_denominator()
        proj_u_on_v.append(fraction)
        print(fraction)

    print('u orthogonal to v: ')
    for i in range(len(u)):
        fraction = Fraction((u[i] - proj_u_on_v[i])).limit_denominator()
        print(fraction)

# Find two vectors in opposite directions that are orthogonal to the vector u. (The answers are not unique. Enter your answer as a comma-separated list of vectors.)
def q8():
    u = [5, -3, 6]

    # find vectors in opposite directions that are orthogonal to the vector u
    vectors = []
    for i in range(-10, 10):
        for j in range(-10, 10):
            for k in range(-10, 10):
                if np.dot(u, [i, j, k]) == 0:
                    vectors.append([i, j, k])

    # check if the vectors are going in opposite directions
    for v in vectors:
        for w in vectors:
            if v[0] == -w[0] and v[1] == -w[1] and v[2] == -w[2]:
                print(v, w)
    # JUST PICK THE ONE BELOW [0, 0, 0] [0, 0, 0].

# A 39,000-pound truck is parked on a 10° slope (see figure). Assume the only force to overcome is that due to gravity. Find the force required to keep the truck from rolling down the hill and the force perpendicular to the hill. (Round your answers to one decimal place.)
def q9():
    truck = 39000
    slope = 10 # in degrees

    # (a) Find the force required to keep the truck from rolling down the hill.
    print(round(truck * np.sin(slope * np.pi / 180), 1))

    # (b) Find the force perpendicular to the hill.
    print(round(truck * np.cos(slope * np.pi / 180), 1))


# A car is towed using a force of 1600 newtons. The chain used to pull the car makes a 27° angle with the horizontal. Find the work done in towing the car 6 kilometers. (Round your answer to one decimal place.)
def q10():
    force = 1600
    distance = 6
    angle = 27
    
    # work done in towing the car 6 kilometers
    print(round(force * distance * np.cos(angle * np.pi / 180), 1))


# this is a shit show because i don't know how it works. Best to move on.
# https://www.chegg.com/homework-help/questions-and-answers/consider-following-yn-x2-y2-x1-3-find-points-intersection-graphs-two-equations-point-x-y-s-q39598719
def q11():
    x = sy.Symbol('x') # x is a symbol

    y1 = x**2
    y2 = x**(1/3)

    # figure out x for which y1 = y2
    solutions = sy.solve(y1 - y2)
    A = solutions[0]
    print(A, ', ', A)
    B = solutions[1]
    print(B, ', ', B)

    y1_diff = y1.diff(x)
    y2_diff = y1.diff(x)


    print('y1 = ', y1_diff.subs(x, A))
    print('y2 = ', y2_diff.subs(x, A))


def test():
    print(Fraction(1, 2))

if __name__ == "__main__":
    q11()
