def fibonacci(n):
    prev_1 = 0
    yield prev_1
    prev_2 = 1
    yield prev_2
    i = 2
    while i < n:
        cur_fib = prev_1 + prev_2
        yield cur_fib
        prev_1 = prev_2
        prev_2 = cur_fib
        i += 1
