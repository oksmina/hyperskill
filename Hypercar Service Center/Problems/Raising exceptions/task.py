class NegativeSumError(Exception):
    pass

def sum_with_exceptions(a, b):
    sum_val = a + b
    if sum_val < 0:
        raise NegativeSumError
    else:
        return sum_val