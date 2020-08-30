import unittest
from pyavl3 import AVLTree


class AVLIteratorTests(unittest.TestCase):

    def test_iterator(self):
        a = AVLTree()
        values = [
            (1, 'a'),
            (2, 'b'),
            (3, 'c'),
        ]
        for k, v in values:
            a[k] = v
        self.assert_list(iter(a), values)

    def test_item_iterator(self):
        a = AVLTree()
        values = [
            (1, 'a'),
            (2, 'b'),
            (3, 'c'),
        ]
        for k, v in values:
            a[k] = v
        self.assert_list(a.items(), values)

    def test_key_iterator(self):
        a = AVLTree()
        values = [
            (1, 'a'),
            (2, 'b'),
            (3, 'c'),
        ]
        for k, v in values:
            a[k] = v

        self.assert_list(a.keys(), [k for k, _ in values])

    def test_value_iterator(self):
        a = AVLTree()
        values = [
            (1, 'a'),
            (2, 'b'),
            (3, 'c'),
        ]
        for k, v in values:
            a[k] = v

        self.assert_list(a.values(), [v for _, v in values])

    def assert_list(self, iterable, expected):
        n = set()
        for val in iterable:
            n.add(val)
            self.assertIn(val, expected)

        self.assertEqual(len(expected), len(n))
