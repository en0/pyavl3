import unittest
from pyavl3 import AVLTree
from pyavl3.traversal import InOrderTraversal

class AVLTreeCopyTest(unittest.TestCase):
    def test_copy_empty(self):
        a = AVLTree()
        b = a.copy()
        self.assertIsNot(a, b)

    def test_copy_contains_same_count(self):
        a = AVLTree(a=1,b=2,c=3)
        b = a.copy()
        self.assertEqual(len(b), 3)

    def test_copy_contains_same_items(self):
        a = AVLTree(a=1, b=2, c=3, d=4, e=5, f=6)
        b = a.copy()
        self.assertListEqual(list(a), list(b))

    def test_copy_doesn_not_reuse_nodes(self):
        a = AVLTree(a=1, b=2, c=3, d=4, e=5, f=6)
        b = a.copy()

        travel_a = InOrderTraversal(a.root, lambda x: x)
        travel_b = InOrderTraversal(b.root, lambda x: x)

        while True:
            _a = next(travel_a, None)
            _b = next(travel_b, None)
            if _a is None and _b is None:
                break;
            self.assertIsNot(_a, _b)

