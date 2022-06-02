import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

    # get the radius
    radius = (1/2)**0.5

    # print the equation
    print("The equation of the sphere with the given characteristics is:", center, radius)

if __name__ == "__main__":
    q4()
