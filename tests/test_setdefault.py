import unittest
from pyavl3 import AVLTree


class AVLTreeSetDefaultTest(unittest.TestCase):
    def test_adds_new_member(self):
        a = AVLTree()
        a.setdefault(1, 'a')
        self.assertEqual(a[1], 'a')

    def test_does_not_add_member(self):
        a = AVLTree({1: 'z'})
        a.setdefault(1, 'a')
        self.assertEqual(a[1], 'z')
        self.assertEqual(len(a), 1)
