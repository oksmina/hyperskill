import numpy as np

row = int(input())
value = int(input())
if value == 0:
    print(np.zeros((row, row)))
else:
    print(np.ones((row, row)))