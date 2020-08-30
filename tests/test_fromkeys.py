import unittest
from pyavl3 import AVLTree


class AVLTreeFromKeysTest(unittest.TestCase):

    def test_creats_new_tree(self):
        a = AVLTree.fromkeys([], None)
        self.assertIsInstance(a, AVLTree)

    def test_from_array(self):
        a = AVLTree.fromkeys([1, 2, 3], None)
        self.assertListEqual(list(a.items()), [(1, None), (2, None), (3, None)])

