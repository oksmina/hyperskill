def check():
    inp = input()
    try:
        value = int(inp)
        if 25 <= value <= 37:
            print(value)
        else:
            print("Correct the error!")
    except ValueError:
        print("Correct the error!")