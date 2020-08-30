import unittest
from pyavl3 import AVLTree


class AVLTreeReprTest(unittest.TestCase):

    def test_empty_create(self):
        a = AVLTree()
        self.assertEqual(str(a), "<AVL {}>")

    def test_1_item(self):
        a = AVLTree(a=1)
        self.assertEqual(str(a), "<AVL {a: 1}>")

    def test_flipped_1_item(self):
        a = AVLTree({1: 'a'})
        self.assertEqual(str(a), "<AVL {1: a}>")

    def test_longer_item(self):
        a = AVLTree([
            # Order of insert is important because
            # repr should do a breadth first traversal.
            ("a", 1), ("b", 2),
            ("c", 3), ("d", 4),
            ("e", 5), ("f", 6),
            ("g", 7), ("g", 7),
        ])

        self.assertEqual(str(a), "<AVL {d: 4, b: 2, f: 6, a: 1, c: 3, e: 5, g: 7}>")
