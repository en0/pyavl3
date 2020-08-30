import unittest
from pyavl3 import AVLTree


class AVLClearTest(unittest.TestCase):

    def test_clear_empty(self):
        a = AVLTree()
        a.clear()

    def test_len_on_clear(self):
        a = AVLTree()
        a[1] = 'a'
        a[2] = 'a'
        a[3] = 'a'
        a.clear()
        self.assertEqual(len(a), 0)

    def test_clear_is_empty(self):
        a = AVLTree()
        a[1] = 'a'
        a[2] = 'a'
        a[3] = 'a'
        a.clear()
        with self.assertRaises(KeyError):
            _ = a[1]
        with self.assertRaises(KeyError):
            _ = a[2]
        with self.assertRaises(KeyError):
            _ = a[3]
