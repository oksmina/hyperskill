enc_mess = input()
key = int(input())
key_b = key.to_bytes(2, byteorder='little')
sum_key = key_b[0] + key_b[1]
res = str()
for ch in enc_mess:
    res += chr(ord(ch) + sum_key)

print(res)