def find_no_overlaps(text, pattern):
    res = []
    i = 0
    while i < len(text) - len(pattern) + 1:
        found = True

        for j, item in enumerate(pattern):
            if text[i + j] != item:
                found = False

        if found:
            res.append(str(i))
            i += len(pattern)
        else:
            i += 1
    return res

result = find_no_overlaps(input(), input())
if result:
    print(' '.join(result))
else:
    print("-1")
