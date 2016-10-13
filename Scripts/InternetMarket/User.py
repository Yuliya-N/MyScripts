from hashlib import md5


class User:
    """
    Basic class for internet market
    """
    optional_fields = {
        'email', 'fname', 'lname', 'address', 'birthday', 'phone'
    }  # set is faster

    def __init__(self, username, **kwargs):
        self.username = username
        for field in User.optional_fields:
            if field in kwargs:
                setattr(self, field, kwargs[field])

    def set_pswd(self, password):
        self.password = 'Not allowed'
        self.pass_hash = md5(password.encode())

    # def __hash__(self):
    #     self.pass_hash = hash(self._password)
    #     return self.pass_hash


# user = User('uname')
# # print(user.pass_hash)
# user.password('123245')
# print(user.password)
# print(user.pass_hash)
