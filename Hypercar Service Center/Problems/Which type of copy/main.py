import copy


def detect_copy():
    obj = [[1, 2], [3, 4]]
    copy_obj = copying_machine(obj)
    return "shallow copy" if id(obj[0]) == id(copy_obj[0]) else "deep copy"
