def selection_sort(elements):
    for i in range(len(elements) - 1):
        index = i

        for j in range(i + 1, len(elements)):
            if len(elements[j]) < len(elements[index]):
                index = j

        el = elements[index]
        elements.pop(index)
        elements.insert(i, el)


count = int(input())
names = []
for _n in range(count):
    names.append(input())

selection_sort(names)
for name in names:
    print(name)