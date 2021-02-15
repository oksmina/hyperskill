class User:
    # create the class attributes
    users = list()
    n_active = 0
    # create the __init__ method
    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name

        User.users.append(user_name)
        User.n_active = 1 if active else 0
