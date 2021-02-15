from collections import deque

n = int(input())
deq = deque()
for _i in range(n):
    input_str = (input()).split()
    if input_str[0] == "ISSUE":
        deq.append(int(input_str[1]))
    if input_str[0] == "SOLVED":
        deq.popleft()

while deq:
    print(deq.popleft())
