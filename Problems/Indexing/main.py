import numpy as np


a = np.array([[1, 3, 4],
              [45, 66, 76],
              [0, 9, 4],
              [12, 14, 90],
              [39, 71, 83],
              [27, 20, 5]])
row = int(input())
value = int(input())
print(a[row, value])