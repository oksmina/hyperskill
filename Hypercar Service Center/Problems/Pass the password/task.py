# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()
passwords.sort(key=len)
for p in passwords:
    print(p, len(p))