numbers = [int(n) for n in input().split()]
target = int(input())
left, right = 0, len(numbers) - 1
result = -1
while left <= right:
    middle = (right + left) // 2
    if target == numbers[middle]:
        result = middle
        right = middle - 1
    elif target < numbers[middle]:
        left = middle + 1
    else:
        right = middle - 1

print(result)
