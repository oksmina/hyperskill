def check(value):
    try:
        value = int(value)
        if value >= 202:
            print(str(value))
        else:
            print("There are less than 202 apples! You cheated on me!")
    except ValueError:
        print("It is not a number!")