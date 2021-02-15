def has_prefix(word, prefix):
    for j, item in enumerate(prefix):
        if word[j] != item:
            return False

    return True


prefix_ = input()
words_ = input().split()

for word_ in words_:
    if has_prefix(word_, prefix_):
        print(word_)