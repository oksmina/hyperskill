def check_email(string):
    if " " in string:
        return False
    if "@" not in string:
        return False
    index_a = string.find("@")
    index_dot = string.find(".", index_a)
    if index_dot != -1 and index_dot > index_a + 1:
        return True
    return False
