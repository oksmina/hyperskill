import copy


def solve(obj):
    copy_obj = copy.deepcopy(obj)
    return not id(obj) == id(copy_obj)