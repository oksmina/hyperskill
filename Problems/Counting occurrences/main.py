def count(numbers, target):
    res = 0
    for i in numbers:
        if i == target:
            res += 1
    return res


numbers_i = input().split(' ')
target_i = input()
print(count(numbers_i, target_i))
