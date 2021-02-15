x = int(input())
lx, rx = (int(n) for n in input().split())
tries = 0

left, right = lx, rx
while left <= right:
    tries += 1
    middle = (left + right) // 2

    if middle == x:
        break
    elif x < middle:
        right = middle - 1
    else:
        left = middle + 1

print(tries)
