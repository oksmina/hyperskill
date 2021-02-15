def count_merge_sort(lst):
    if len(lst) < 2:
        return 0

    mid = len(lst) // 2
    left = count_merge_sort(lst[:mid])
    right = count_merge_sort(lst[mid:])

    return left + right + 1

merge_list = input().split()
print(count_merge_sort(merge_list))