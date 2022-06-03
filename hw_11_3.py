import numpy as np

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
    B = (10,4,11)
    C = (12,7,4)
    D = (3,4,-4)

    AB = (B[0] - A[0], B[1] - A[1], B[2] - A[2])
    DC = (C[0] - D[0], C[1] - D[1], C[2] - D[2])
    BC = (C[0] - B[0], C[1] - B[1], C[2] - B[2])
    AD = (D[0] - A[0], D[1] - A[1], D[2] - A[2])

    # AB and AD are adjacent sides.
    AB_x_AD = np.cross(AB, AD)

    print('sqrt(', (np.linalg.norm(AB_x_AD) ** 2), ')')




def test():
    pass

if __name__ == "__main__":
    q5()
