# mystery_set has been defined
string = input()
while string in mystery_set:
    mystery_set.discard(string)
# delete string from mystery_set