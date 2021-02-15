def find_last(text, pattern):
    for i in range(len(text) - len(pattern), -1, -1):
        found = True

        for j, item in enumerate(pattern):
            if text[i + j] != item:
                found = False
                break

        if found:
            return i

    return -1


print(find_last(input(), input()))