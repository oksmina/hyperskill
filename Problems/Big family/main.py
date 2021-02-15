# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

new_dict = dict()
new_dict.update(first_family)
new_dict.update(second_family)
# Work with the 'first_family' and 'second_family' and create a new dictionary
print(new_dict)