import unittest
from User import User
from hashlib import md5


class UserTestCase(unittest.TestCase):
    def test_basic(self):
        u = User('user1', 'ashgdhsfv', email='user1@gmail.com')
        self.assertEqual(u.username, 'user1')
        self.assertEqual(u.email, 'user1@gmail.com')
        self.assertNotEqual(u.password, 'ashgdhsfv')
        # check that it uses by folder>python -m unittest
        # self.assertEqual(1,2)

    def test_skip_optional(self):
        u = User('user2', 'ashgdhsfv', email='user1@gmail.com', fax='+380671412')
        self.assertFalse(hasattr(u, 'fax'))
        # check that it uses by folder>python -m unittest
        # self.assertEqual(1 in {3, 2}, False)

    def test_create_with_pswd(self):
        user = User('user1', password='QAZWSX!@')
        self.assertTrue(hasattr(user, 'pass_hash'))
        self.assertEqual(user.pass_hash, md5(b'QAZWSX!@').hexdigest())
        # print(md5('QAZWSX!@'.encode()))
        # print(md5(b'QAZWSX!@'))

        # self.assertIn(1, {3, 2})  # better error descr
        # self.assertEqual(1 in {3, 2}, False)

    def test_set_password(self):
        user = User('user1', password='QAZWSX!@')
        user.password ='QAZWSX!@'
        self.assertTrue(hasattr(user, 'pass_hash'))
        self.assertTrue(hasattr(user, 'password'))

    def test_set_attr(self):
        user = User('user1', password='QAZWSX!@')
        # useful when we expect the exception to be raised
        # with self.assertRaises(AttributeError):
        #     user.password = 'QWERTY'


if __name__ == '__main__':
    unittest.main()


# The same with simple assers
# u = User('user1', 'ashgdhsfv', email='user1@gmail.com')
# assert u.username == 'user1'
# assert u.pass_hash == 'ashgdhsfv'
# assert u.email == 'user1@gmail.com'
# u2 = User(
#     'user2', 'ashgdhsfv', email='user1@gmail.com', fax='+380677931412'
# )
# assert not hasattr(u2, 'fax'), 'No such attribute'
# assert u.username == u2.username, (u.username, u2.username)
