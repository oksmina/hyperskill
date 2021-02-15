numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
number_file = open("file_with_list.txt", "w")
print(numbers, sep=" ", end='', file=number_file)
number_file.close()
