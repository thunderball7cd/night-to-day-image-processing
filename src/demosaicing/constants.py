import numpy as np


filter0 = np.array([
    [ 0, 0, -1, 0,  0],
    [ 0, 0,  2, 0,  0],
    [-1, 2,  4, 2, -1],
    [ 0, 0,  2, 0,  0],
    [ 0, 0, -1, 0,  0]
], dtype=np.float32)


filter1 = np.array([
    [ 0,  0,  1,  0,  0],
    [ 0, -2,  0, -2,  0],
    [-2,  8, 10,  8, -2],
    [ 0, -2,  0, -2,  0],
    [ 0,  0,  1,  0,  0]
], dtype=np.float32)


filter2 = np.array([
    [ 0,  0, -2,  0,  0],
    [ 0, -2,  8, -2,  0],
    [ 1,  0, 10,  0,  1],
    [ 0, -2,  8, -2,  0],
    [ 0,  0, -2,  0,  0]
], dtype=np.float32)


filter3 = np.array([
    [ 0,  0, -3,  0,  0],
    [ 0,  4,  0,  4,  0],
    [-3,  0, 12,  0, -3],
    [ 0,  4,  0,  4,  0],
    [ 0,  0, -3,  0,  0]
], dtype=np.float32)


