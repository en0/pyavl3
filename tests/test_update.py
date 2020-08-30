import unittest
from pyavl3 import AVLTree


class AVLTreeUpdateTest(unittest.TestCase):
    def test_add_one(self):
        a = AVLTree()
        a.update({1:'a'})
        self.assertEqual(len(a), 1)
