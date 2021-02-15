# the object_list has already been defined
# write your code here
from collections.abc import Hashable
hash_dict = dict()

for obj in object_list:
    if isinstance(obj, Hashable):
        cur_hash = hash(obj)
        hash_dict.setdefault(cur_hash, 0)
        hash_dict[cur_hash] += 1

count_hash = 0
for hash_obj in hash_dict.values():
    if hash_obj != 1:
        count_hash += hash_obj

print(count_hash)