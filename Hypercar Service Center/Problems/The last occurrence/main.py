def search(numbers, target):
    for i, elem in reversed(list(enumerate(numbers))):
        if elem == target:
            return i

    return -1


numbers_i = input().split(' ')
target_i = input()
print(search(numbers_i, target_i))