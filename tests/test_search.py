import unittest
from pyavl3 import AVLTree
from pyavl3.search import (
    GreatherThanSearch,
    GreatherThanOrEqualSearch,
    LessThanSearch,
    LessThanOrEqualSearch,
    BetweenSearch,
)



class SearchAlgorithmTest(unittest.TestCase):
    def setUp(self):
        self.values = [
            (1, 'a'), (2, 'b'),
            (3, 'c'), (4, 'd'),
            (5, 'e'), (6, 'f'),
            (7, 'g'), (8, 'g'),
        ]
        self.cases = [
            (GreatherThanSearch(3), filter(lambda x: x[0] > 3, self.values)),
            (GreatherThanOrEqualSearch(3), filter(lambda x: x[0] >= 3, self.values)),
            (LessThanSearch(5), filter(lambda x: x[0] < 5, self.values)),
            (LessThanOrEqualSearch(5), filter(lambda x: x[0] <= 5, self.values)),
            (BetweenSearch(3, 6), filter(lambda x: 3 < x[0] < 6, self.values)),
        ]

    def test_algos(self):
        for algo, expected in self.cases:
            with self.subTest(algo):
                a = AVLTree(self.values)
                self.assertListEqual(list(algo(a)), list(expected))

    def test_algos_empty(self):
        for algo, _ in self.cases:
            with self.subTest(algo):
                a = AVLTree()
                self.assertListEqual(list(algo(a)), [])
