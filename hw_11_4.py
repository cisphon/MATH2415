import numpy as np

# Find the cross product of the unit vectors.
def q1():
    print('just use gpt-3 and don\'t use a regular k. Use a vector k.')

def q2():

    u = [6, 5, -5]
    v = [8, -9, 1]

    print(np.cross(u, v))
    print(np.cross(v, u))
    print(np.cross(v, v))

def q3():
    u = [1, 1, 1]
    v = [2, 1, -1]

    print(np.cross(u, v))

    # Determine if u × v is orthogonal to both u and v by finding the values below.
    a = np.dot(np.cross(u, v), u)
    print(a)
    b = np.dot(np.cross(u, v), v)
    print(b)

    if(a == 0 and b == 0):
        print("u and v are orthogonal")

# Find a unit vector that is orthogonal to both u and v.
def q4():
    u = [-8, -6, 4]
    v = [17, -18, -1]

    print('Just put the vector over the sqrt(x)')

    print(np.cross(u, v))

    # get the norm of u x v
    print('sqrt(', (np.linalg.norm(np.cross(u, v)) ** 2), ')')

# Verify that the points are the vertices of a parallelogram, and find its area.
def q5():
    A = (1,1,3)
    B = (2, -1, 12)
    C = (4,2,5)
    D = (3, 4, -4)

    AB = (B[0] - A[0], B[1] - A[1], B[2] - A[2])
    DC = (C[0] - D[0], C[1] - D[1], C[2] - D[2])
    BC = (C[0] - B[0], C[1] - B[1], C[2] - B[2])
    AD = (D[0] - A[0], D[1] - A[1], D[2] - A[2])

    # AB and AD are adjacent sides.
    AB_x_AD = np.cross(AB, AD)

    print('sqrt(', (np.linalg.norm(AB_x_AD) ** 2), ')')

# Find the area of the triangle with the given vertices. 
def q6():
    A = (0,0,0)
    B = (3,0,7)
    C = (-7,6,0)

    AB = (B[0] - A[0], B[1] - A[1], B[2] - A[2])
    AC = (C[0] - A[0], C[1] - A[1], C[2] - A[2])

    AB_x_AC = np.cross(AB, AC)

    print('sqrt(', (np.linalg.norm(AB_x_AC) ** 2), ')/2')

# Both the magnitude and the direction of the force on a crankshaft change as the crankshaft rotates. Find the magnitude of the torque on the crankshaft using the position and data shown in the figure, where F = 1200 lb.
def q7():
    lb = 1200

    PQ = [0, 0, 0.16]


    # https://www.wolframalpha.com/input?i=cos%28-30%29
    j = np.sqrt(3) / 2 # -30 degrees
    k = -1/2 # -30 degrees
    
    F = np.dot(lb, [0, j, k])

    PQ_x_F = np.cross(PQ, F) / np.sqrt(3)

    PQ_x_F_norm = np.linalg.norm(PQ_x_F)

    print(PQ_x_F_norm, 'sqrt(3)')

# Find u · (v × w).
def q8():
    u = [1, 0, 0]
    v = [0, 1, 0]
    w = [0, 0, 1]
    print(np.dot(u, np.cross(v, w)))

# Find u · (v × w).
def q9():
    u = [4, 0, 0]
    v = [9, 9, 9]
    w = [0, 4, 4]
    print(np.dot(u, np.cross(v, w)))

# Use the triple scalar product to find the volume of the parallelepiped having adjacent edges u, v, and w.
def q10():
    u = [1, 1, 0]
    v = [0, 1, 1]
    w = [1, 0, 1]

    print(np.dot(u, np.cross(v, w)))

def test():
    pass

if __name__ == "__main__":
    q7()
