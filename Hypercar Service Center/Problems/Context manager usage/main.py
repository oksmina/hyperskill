# write your code here
lib = shelve.open("my_library", flag="c", writeback=False)
lib["Anna Karenina"] = "Happy families are all alike; every unhappy family is unhappy in its own way..."
print("A new book has been added to the library!")