num = int(input())
num_b = num.to_bytes(2, byteorder='little')
print(num_b[0] + num_b[1])
