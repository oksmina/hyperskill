num = input()

my_generator = (int(d) for d in num)

sum_d = 0
for d in my_generator:
    sum_d += d
print(sum_d)