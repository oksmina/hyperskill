from collections.abc import Hashable
# create your dictionary here
objects_dict = dict()
for o in objects:
    if isinstance(o, Hashable):
        objects_dict[o] = hash(o)