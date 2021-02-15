f_str = input()
s_str = input()
res = str()
for f, s in zip(f_str, s_str):
    res += f
    res += s
print(res)
