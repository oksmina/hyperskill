# read sample.txt and print the number of lines
f = open("sample.txt", "r")
i = 0
for line in f:
    i += 1
f.close()
print(i)