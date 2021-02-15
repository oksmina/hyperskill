# the list "walks" is already defined
# your code here

sum = 0
for w in walks:
    sum = sum + w["distance"]

print(sum // len(walks))