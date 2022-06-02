import numpy as np
import sympy as sy
from scipy.linalg import qr

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
        print('u and v are not orthogonal or parallel')



def q5():


# Consider the following.
def q7():
    u = np.array([2, 3])
    v = np.array([7, 5])

    # projection of u onto v
    print(np.dot(u, v) / np.linalg.norm(v))


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

if __name__ == "__main__":
    q3()
