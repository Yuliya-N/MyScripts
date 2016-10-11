class User:
    """
    Basic class for internet market
    """
    optional_fields = {
        'email', 'fname', 'lname', 'address', 'birthday', 'phone'
    }  # set is faster

    def __init__(self, username, pass_hash, **kwargs):
        self.username = username
        self.pass_hash = pass_hash
        for field in User.optional_fields:
            if field in kwargs:
                setattr(self, field, kwargs[field])
