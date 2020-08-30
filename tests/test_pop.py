import unittest
from pyavl3 import AVLTree


class AVLTreePopItemTest(unittest.TestCase):
    def test_pop_raises_keyerror(self):
        a = AVLTree()
        with self.assertRaises(KeyError):
            a.pop(1)

    def test_pop_returns_value_for_key(self):
        a = AVLTree({1:'a'})
        self.assertEqual(a.pop(1), 'a')

    def test_pop_removes_member(self):
        a = AVLTree({1:'a'})
        a.pop(1)
        with self.assertRaises(KeyError):
            a[1]

    def test_pop_updates_len(self):
        a = AVLTree({1:'a'})
        a.pop(1)
        self.assertEqual(len(a), 0)
