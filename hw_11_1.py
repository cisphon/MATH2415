import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Plot the points on the same three-dimensional coordinate system.
# (a) (4, 3, 1)
# (b) (-1, 5, 2)
def q1():
    # get the points
    p1 = (4, 3, 1)
    p2 = (-1, 5, 2)

    # 5 inches by 5 inches
    fig = plt.figure()
    fig.set_figheight(5)
    fig.set_figwidth(5)
    
    # make it 3d
    ax = fig.add_subplot(111, projection='3d')

    # plot the points
    ax.scatter(p1[0], p1[1], p1[2], c='r', marker='o')
    ax.scatter(p2[0], p2[1], p2[2], c='b', marker='o')

    # set the labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # set the limits of the axes
    ax.axes.set_xlim3d(-10, 10)
    ax.axes.set_ylim3d(-10, 10)
    ax.axes.set_zlim3d(0, 10)

    # rotate the plot
    ax.view_init(45, 45)

    # show the plot
    plt.show()


# Find the distance d between the points (-2, 2, 2) and (-6, 3, -6).
def q2():
    p1 = (-2, 2, 2)
    p2 = (-6, 3, -6)

    # get the distance between the two points
    dist = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

    # print the distance
    print("The distance between the two points is:", dist)

# Find the corrdinates of the midpoint of the line segment joining the points (6, 0, -5) and (8, 4, 23).
def q3():
    p1 = (6, 0, -5)
    p2 = (8, 4, 23)

    # get the midpoint
    midpoint = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2, (p1[2] + p2[2])/2)

    # print the midpoint
    print("The midpoint of the line segment joining the points is:", midpoint)

# Find the standard equation of the sphere with the given characteriststics.
# Center: (-3, 0, 0), tangent to the yz-plane
def q4():
    # get the center
    center = (-3, 0, 0)

    radius = ((center[0]**2 + center[1]**2 + center[2]**2)**0.5)

    print('(x -', center[0], ')^2 + (y -', center[1], ')^2 + (z -', center[2], ')^2 =', radius**2)

# Consider the following.
def q5():
    start = (4, 2, 1)
    end = (2, 4, 3)

    # get the vector between the two points
    vector = (end[0] - start[0], end[1] - start[1], end[2] - start[2])

    print(vector)

    print('standard vector notation needs to use the vector symbols for i, j, and k instead of regular i, j, and k')

# The initial and terminal points of a vector v are given.
def q6():

    start = (-1, 4, 5)
    end = (5, 5, 6)

    # get the vector between the two points
    vector = (end[0] - start[0], end[1] - start[1], end[2] - start[2])

    print(vector)

def q7():
    start = (2, 8, 0)
    end = (4, 1, 8)

    # get the vector between the two points
    vector = (end[0] - start[0], end[1] - start[1], end[2] - start[2])

    print(vector)

    # get the magnitude of the vector
    print('sqrt(', vector[0]**2 + vector[1]**2 + vector[2]**2, ')')

    # for the last one, just put the magnitude under the vector.

def q8():
    u = [1, 2, 3]
    v = [2, 2, -1]
    w = [4, 0, -4]

    # 9u - 3v - 1/2w

    print(np.dot(u, 9) - np.dot(v, 3) - np.dot(w, 0.5))

    
# Determine which of the vectors is (are) parallel to z. Use a graphing utility to confirm your results. (Select all that apply.)
def q9():
    z = [5, 4, -7]

    a = [-10, -8, 14]
    b = [2, 8/5, -14/5]
    c = [10, 8, 14]
    d = [1, -8, 4]

    print('Just check which numbers are all the same (they\'ll be parallel).')
    print(z[0]/a[0], ' ', z[1]/a[1], ' ', z[2]/a[2])
    print(z[0]/b[0], ' ', z[1]/b[1], ' ', z[2]/b[2])
    print(z[0]/c[0], ' ', z[1]/c[1], ' ', z[2]/c[2])
    print(z[0]/d[0], ' ', z[1]/d[1], ' ', z[2]/d[2])


# Use vectors to determine whether the points are collinear.
def q10():
    P = (0, -2, -5)
    Q = (10, 13, 15)
    R = (4, 4, 3)

    # get the vectors
    PQ = (Q[0] - P[0], Q[1] - P[1], Q[2] - P[2])
    PR = (R[0] - P[0], R[1] - P[1], R[2] - P[2])
 
        
    if ((PQ[0] / PR[0]) == (PQ[1] / PR[1]) == (PQ[2] / PR[2])):
        print("The vectors are parallel (therefore the points are collinear).")


# Find a unit vector in the direction of v and in the direction opposite of v.
def q11():
    v = [1, -9, -8]

    # (a) in the direction of v
    # v / ||v||
    print('sqrt(', v[0] ** 2 + v[1] ** 2 + v[2] ** 2, ')')

    print(v)

    # (b) in the direction opposite of v
    # -v / ||v||

    
    # multiply each element by -1
    v_opp = [-v[0], -v[1], -v[2]]

    print(v_opp)

    print('divide each vector by sqrt(x) and input them as a vector.')

# The guy wire supporting a 100-foot tower has a tension of 500 pounds. Using the distances shown in the figure, write the component form of the vector F representing the tension in the wire. (Round your answers to three decimal places.)
def q12():

    pounds = 560

    # the point is where the guy wire tower is located relative to the top of the tower.
    # that means we put -100 instead of 100.
    guy_wire = (75, -50, -100)

    # magnitude of the guy wire
    guy_wire_magnitude = (guy_wire[0]**2 + guy_wire[1]**2 + guy_wire[2]**2)
    c_squared = (pounds**2 / guy_wire_magnitude)

    # get c and round to 3 decimal places
    c = round(c_squared**0.5, 3)

    print('if the number is 123.1 then the number is 123.100')
    print('don\'t use the i j k notation')
    print(round(guy_wire[0]*c, 3), 'i ', round(guy_wire[1]*c, 3), 'j ', round(guy_wire[2]*c, 3), 'k')

def test():
    pass

if __name__ == "__main__":
    q12()
