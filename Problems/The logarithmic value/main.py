import math

n = int(input())
base = int(input())
if n == 0:
    print(n)
elif base > 1:
    print(round(math.log(n, base), 2))
else:
    print(round(math.log(n), 2))
