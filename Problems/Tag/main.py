def tagged(other_func):
    def wrapper(string):
        cur_str = other_func(string)
        return f"<title>{cur_str}</title>"

    return wrapper