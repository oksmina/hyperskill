# put your python code here
from collections import deque

brackets = deque()
inp = input()

err = False
for n in inp:
    if n == "(":
        brackets.append(n)
    elif n == ")":
        if brackets:
            brackets.pop()
        else:
            err = True

if not err and len(brackets) == 0:
    print("OK")
else:
    print("ERROR")