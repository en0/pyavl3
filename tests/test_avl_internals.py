import unittest
from pyavl3 import AVLTree


class AVLTreeInternalsTest(unittest.TestCase):

    def test_get_min(self):
        import random
        a = AVLTree()
        m = None
        for _ in range(100):
            r = random.randint(-9999, 9999)
            m = min(r, m or r)
            a[r] = 'a'
        self.assertEqual(a._get_min(a.root).key, m)

    def test_get_min_is_root(self):
        a = AVLTree()
        a[5] = 'a'
        self.assertEqual(a._get_min(a.root).key, 5)

    def test_get_min_is_left_of_root(self):
        a = AVLTree()
        a[5] = 'a'
        a[4] = 'a'
        self.assertEqual(a._get_min(a.root).key, 4)

    def test_get_min_is_left_of_root2(self):
        a = AVLTree()
        a[5] = 'a'
        a[1] = 'a'
        a[4] = 'a'
        a[3] = 'a'
        a[2] = 'a'
        self.assertEqual(a._get_min(a.root).key, 1)

    def test_pop_right_min_returns_min(self):
        a = AVLTree()
        a[5] = 'a'
        a[1] = 'a'
        a[9] = 'a'
        a[8] = 'a'
        self.assertEqual(a._pop_right_min(a.root).key, 8)

    def test_pop_right_min_removes_min(self):
        a = AVLTree()
        a[5] = 'a'
        a[1] = 'a'
        a[9] = 'a'
        a[8] = 'a'
        self.assertIsNotNone(a.root.right.left)
        a._pop_right_min(a.root)
        self.assertIsNone(a.root.right.left)

    def test_pop_right_min_removes_min_and_keeps_children(self):
        a = AVLTree()
        a[5] = 'a'
        a[1] = 'a'
        a[8] = 'a'
        a[9] = 'a'
        self.assertEqual(a.root.right.key, 8)
        a._pop_right_min(a.root)
        self.assertEqual(a.root.right.key, 9)
