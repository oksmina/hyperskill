from collections import deque

n = int(input())
my_book = deque()
red_book = list()
for _n in range(n):
    inp = input()
    if inp != "READ":
        act, book = inp.split(" ", 1)
    else:
        act = inp

    if act == "BUY":
        my_book.append(book)
    elif act == "READ":
        red_book.append(my_book.pop())

for b in red_book:
    print(b)