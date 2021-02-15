def min_max_sort(elements):
    for i in range(len(elements) - 1):
        index = i

        if i % 2 == 0:
            for j in range(i + 1, len(elements)):
                if elements[j] < elements[index]:
                    index = j
        else:
            for j in range(i + 1, len(elements)):
                if elements[j] > elements[index]:
                    index = j

        elements[i], elements[index] = elements[index], elements[i]

numbers = [int(n) for n in input().split()]
min_max_sort(numbers)
numbers_str = [str(n) for n in numbers]
print(" ".join(numbers_str))