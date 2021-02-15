# use the function blackbox(lst) that is already defined
lst1 = [0, 0, 2, 1]
id1 = id(lst1)
lst2 = blackbox(lst1)
id2 = id(lst2)
print("modifies" if (id1 == id2) else "new")