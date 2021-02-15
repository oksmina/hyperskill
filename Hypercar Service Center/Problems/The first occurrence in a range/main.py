def search(numbers, target, a, b):
    a = int(a)
    b = int(b)
    for i, elem in enumerate(numbers):
        if a <= i < b:
            if elem == target:
                return i
    return -1


numbers_in = input().split()
target_in = input()
a_in, b_in = input().split()
print(search(numbers_in, target_in, a_in, b_in))