from collections import deque

n = int(input())
deq_ready = deque()
for _i in range(n):
    input_str = (input()).split()
    if input_str[0] == "READY":
        deq_ready.append(input_str[1])
    if input_str[0] == "EXTRA":
        cur = deq_ready.popleft()
        deq_ready.append(cur)
    if input_str[0] == "PASSED":
        print(deq_ready.popleft())
