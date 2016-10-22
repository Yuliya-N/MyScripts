from hashlib import md5

# class Password:
#     # def __init__
#     def __get__(self, obj, objtype):
#         print('Calling __get__')
#         print('Obj is {}'.format(obj))
#         print('Objtype is {}'.format(objtype))
#         return 42

#     def __set__(self, obj, value):
#         print('Calling __set__')
#         print('Obj is {}'.format(obj))
#         print('Value is {}'.format(value))

#     # def __del__(self, obj, objtype):
#     #     print('Calling __set__')
#     #     print('Obj is {}'.format(obj))
#     #     print('Objtype is {}'.format(objtype))

class User:
    """
    Basic class for internet market
    """
    optional_fields = {
        'email', 'fname', 'lname', 'address', 'birthday', 'phone'
    }  # set is faster

    def __init__(self, username, password, **kwargs):
        self.username = username
        # descriptor works here, not a simple =
        self.password = password
        for field in User.optional_fields:
            if field in kwargs:
                setattr(self, field, kwargs[field])

    @property
    def password(self):
        return '<Password with hash {}>'.format(self.pass_hash)

    # @password.deleter
    # @password.getter

    # descriptor
    # password = property(get_pswd, set_pswd)

    @password.setter
    def password(self, password):
        self.pass_hash = md5(password.encode()).hexdigest()


# user = User('name', 'qwerty')
# print(user.password)
# user.password = 'ASDFGH'
# print(user.password)

