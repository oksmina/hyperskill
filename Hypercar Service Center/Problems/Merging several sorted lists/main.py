def merge(left, right):
    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1

    return merged


def merge_multi(lists):
    res = []
    for i, _el in enumerate(lists):
        res = merge(res, lists[i])
    return res


count = int(input())
in_lists = []
for _i in range(count):
    in_lists.append([int(x) for x in input().split()])

mege_list = merge_multi(in_lists)
print(" ".join([str(x) for x in mege_list]))
