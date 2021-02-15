def choose_median(lst, start, middle, end):
    if lst[start] <= lst[middle]:
        if lst[middle] <= lst[end]:
            return middle
        elif lst[start] <= lst[end]:
            return end
        else:
            return start
    else:
        if lst[middle] >= lst[end]:
            return middle
        elif lst[start] <= lst[end]:
            return start
        else:
            return end


def partition(lst, pivot, start, end):
    j = start
    lst[pivot], lst[start] = lst[start], lst[pivot]

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


_lst = [int(x) for x in input().split()]
mid = len(_lst) // 2 if len(_lst) % 2 == 1 else len(_lst) // 2 - 1
_pivot = choose_median(_lst, 0, mid, len(_lst) - 1)
print(_pivot)
partition(_lst, _pivot, 0, len(_lst) - 1)
print(' '.join([str(x) for x in _lst]))