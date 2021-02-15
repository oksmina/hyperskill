# put your python code here
def partition(lst, start, end):
    j = start
    for i in range(start + 1, end + 1):
        if lst[i] < lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    k = j
    for i in range(start + 1, end + 1):
        if lst[i] == lst[start]:
            k += 1
            lst[i], lst[k] = lst[k], lst[i]
    lst[start], lst[j] = lst[j], lst[start]

    return j, k


in_list = [int(x) for x in input().split()]
pivot = in_list[0]
start_, end_ = partition(in_list, 0, len(in_list) - 1)
print(start_, end_)
print(" ".join([str(x) for x in in_list]))
