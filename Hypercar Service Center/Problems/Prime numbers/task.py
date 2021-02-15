prime_numbers = list()
for i in range(2, 1000):
    if all(i % x for x in prime_numbers):
        prime_numbers.append(i)
