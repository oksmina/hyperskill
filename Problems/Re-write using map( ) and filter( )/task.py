even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Re-write the rest of the code here using map() and filter() where possible
my_sum = map(lambda e, o: e + o, even, odd)

remainders = map(lambda x: x % 3, my_sum)

nonzero_remainders = list(filter(lambda r: r, remainders))