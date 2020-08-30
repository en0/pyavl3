import unittest
from pyavl3 import AVLTree


class AVLCreatTest(unittest.TestCase):

    def test_empty_create(self):
        a = AVLTree()
        self.assertEqual(len(a), 0)

    def test_iterable_create(self):
        a = AVLTree([(1, 'a'), (2, 'b'), (3, 'c')])
        self.assertEqual(len(a), 3)

    def test_iterable_create_by_dict(self):
        a = AVLTree({1: 'a', 2: 'b', 3: 'c'})
        self.assertEqual(len(a), 3)

    def test_iterable_create_by_kwargs(self):
        a = AVLTree(
            a='a',
            b='b',
            c='c',
        )
        self.assertEqual(len(a), 3)

    def test_iterable_create_by_both(self):
        a = AVLTree([('a', 'a'), ('b', 'b')], c='c')
        self.assertEqual(len(a), 3)
