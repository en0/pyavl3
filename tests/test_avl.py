import unittest
from pyavl3 import AVLTree


class AVLTreeTest(unittest.TestCase):

    def test_insert(self):
        a = AVLTree()
        a[1] = "hello"
        a[2] = "world"

    def test_getitem(self):
        a = AVLTree()
        a[1] = "hello"
        a[2] = "world"
        self.assertEqual(a[1], "hello")
        self.assertEqual(a[2], "world")

    def test_getitem_raises_key_error(self):
        a = AVLTree()
        with self.assertRaises(KeyError):
            _ = a[1]

    def test_get_does_not_raise_key_error(self):
        a = AVLTree()
        _ = a.get(1)

    def test_get_returns_default(self):
        a = AVLTree()
        s = object()
        v = a.get(1, s)
        self.assertIs(s, v)

    def test_contains(self):
        a = AVLTree()
        a[1] = 'a'
        a[2] = 'a'
        a[3] = 'a'
        self.assertTrue(1 in a)
        self.assertTrue(2 in a)
        self.assertTrue(3 in a)

    def test_not_contains(self):
        a = AVLTree()
        a[1] = 'a'
        a[2] = 'a'
        a[3] = 'a'
        self.assertFalse(0 in a)
        self.assertFalse(4 in a)

    def test_traversal_on_left_heavy(self):
        a = AVLTree()
        a[3] = "a"
        a[2] = "b"
        a[1] = "c"
        self.assertListEqual([1,2,3], [k for k, _ in a])

    def test_traversal_on_right_heavy(self):
        a = AVLTree()
        a[1] = "a"
        a[2] = "b"
        a[3] = "c"
        self.assertListEqual([1,2,3], [k for k, _ in a])

    def test_traversal_on_balanced(self):
        a = AVLTree()
        a[2] = "a"
        a[1] = "b"
        a[3] = "c"
        self.assertListEqual([1,2,3], [k for k, _ in a])

    def test_len_on_left_heavy(self):
        a = AVLTree()
        a[3] = "a"
        a[2] = "a"
        a[1] = "a"
        self.assertEqual(len(a), 3)

    def test_len_on_right_heavy(self):
        a = AVLTree()
        a[1] = "a"
        a[2] = "a"
        a[3] = "a"
        self.assertEqual(len(a), 3)

    def test_len_on_balanced(self):
        a = AVLTree()
        a[2] = "a"
        a[1] = "a"
        a[3] = "a"
        self.assertEqual(len(a), 3)

    def test_len_on_left_right(self):
        a = AVLTree()
        a[5] = "a"
        a[3] = "a"
        a[4] = "a"
        self.assertEqual(len(a), 3)

    def test_len_on_right_left(self):
        a = AVLTree()
        a[5] = "a"
        a[7] = "a"
        a[6] = "a"
        self.assertEqual(len(a), 3)

    def test_depth_3_nodes(self):
        a = AVLTree()
        a[2] = "a"
        a[1] = "a"
        a[3] = "a"
        self.assertEqual(a._root.height, 1)

    def test_depth_7_nodes(self):
        a = AVLTree()
        a[1] = "a"
        a[2] = "a"
        a[3] = "a"
        a[4] = "a"
        a[5] = "a"
        a[6] = "a"
        a[7] = "a"
        self.assertEqual(a._root.height, 2)

    def test_depth_8_nodes(self):
        a = AVLTree()
        a[1] = "a"
        a[2] = "a"
        a[3] = "a"
        a[4] = "a"
        a[5] = "a"
        a[6] = "a"
        a[7] = "a"
        a[8] = "a"
        self.assertEqual(a._root.height, 3)

    def test_left_right_balance(self):
        a = AVLTree()
        a[5] = 'a'
        a[3] = 'a'
        a[4] = 'a'
        self.assertEqual(a._root.height, 1)

    def test_right_left_balance(self):
        a = AVLTree()
        a[5] = 'a'
        a[7] = 'a'
        a[6] = 'a'
        self.assertEqual(a._root.height, 1)

    def test_update_in_place(self):
        a = AVLTree()
        a[1] = 'a'
        a[2] = 'b'
        a[3] = 'a'
        self.assertEqual(a[2], "b")
        a[2] = 'c'
        self.assertEqual(a[2], "c")
        self.assertEqual(len(a), 3)
