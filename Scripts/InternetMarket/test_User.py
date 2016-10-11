import unittest
from User import User


class UserTestCase(unittest.TestCase):
    def test_basic(self):
        u = User('user1', 'ashgdhsfv', email='user1@gmail.com')
        # assert u.username == 'user1'
        self.assertEqual(u.username, 'user1')
        # assert u.pass_hash == 'ashgdhsfv'
        self.assertEqual(u.pass_hash, 'ashgdhsfv')
        # assert u.email == 'user1@gmail.com'
        self.assertEqual(u.email, 'user1@gmail.com')
        # self.assertEqual(1,2)  # check that it uses by folder>python -m unittest

    def test_skip_optional(self):
        u = User(
            'user2', 'ashgdhsfv', email='user1@gmail.com', fax='+380677931412'
        )
        # assert not hasattr(u2, 'fax'), 'No such attribute'
        # self.assertEqual(hasattr(u, 'fax'), False)
        self.assertFalse(hasattr(u, 'fax'))
        self.assertIn(1, {3, 2})  # better error descr
        self.assertEqual(1 in {3, 2}, False)


if __name__=='__main__':
    unittest.main()

# u = User('user1', 'ashgdhsfv', email='user1@gmail.com')
# assert u.username == 'user1'
# assert u.pass_hash == 'ashgdhsfv'
# assert u.email == 'user1@gmail.com'
# u2 = User(
#     'user2', 'ashgdhsfv', email='user1@gmail.com', fax='+380677931412'
# )
# assert not hasattr(u2, 'fax'), 'No such attribute'
# assert u.username == u2.username, (u.username, u2.username)
