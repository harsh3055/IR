import math
import numpy as np
from math import cos as c
from math import sin as s

# Input DH parameters
dh_table = np.zeros((7, 4))
for i in range(7):
    parameters = np.array(list(map(int, input("Enter parameters of " + str(i) + "th link ").strip().split())))
    dh_table[i] = parameters


# i is subscript and j is superscript for T
def T(i, j):
    theta_i = math.radians(dh_table[i][3])
    a_j = dh_table[j][1]
    alpha_j = math.radians(dh_table[j][0])
    d_i = dh_table[i][2]
    return np.array([[c(theta_i), -s(theta_i), 0, a_j],
                     [c(alpha_j) * s(theta_i), c(alpha_j) * c(theta_i), -s(alpha_j), -d_i * s(alpha_j)],
                     [s(alpha_j) * s(theta_i), s(alpha_j) * c(theta_i), c(alpha_j), d_i * c(alpha_j)],
                     [0, 0, 0, 1]])


def final_transformation_matrix():
    mat = T(1, 0)
    for i in range(2, 7):
        mat = np.matmul(mat, T(i, i - 1))
    return mat


point_coords = np.array([0, 0, 0, 1])
print(np.matmul(final_transformation_matrix(), point_coords))