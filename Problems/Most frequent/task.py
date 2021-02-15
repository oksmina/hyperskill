from collections import Counter
text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

n = int(input())
word_counter = Counter(text.split())
for val, count in word_counter.most_common(n):
    print(f"{val} {count}")
