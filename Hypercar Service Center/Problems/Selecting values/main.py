import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())
ar = np.array([a, b, c, d])
spec = np.where(ar >= 45)
print(ar[spec])