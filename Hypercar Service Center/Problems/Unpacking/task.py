def unpack(input_tuple):
    unpacked = ()
    for el in input_tuple:
        if isinstance(el, tuple):
            unpacked += el
        else:
            unpacked += (el,)
    return unpacked