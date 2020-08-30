import unittest
from pyavl3.avl_node import AVLNode
from pyavl3.traversal import BreadthFirstTraversal


class BreadthFirstTest(unittest.TestCase):
    def test_small(self):
        a = AVLNode('a', 1)
        b = AVLNode('b', 2)
        c = AVLNode('c', 3)

        a.left = b
        a.right = c

        self.assertListEqual(
            [a, b, c],
            [x for x in BreadthFirstTraversal(a, lambda x: x)]
        )

    def test_small(self):

        # Using the fact that a binary tree stored in
        # array format is ordered in breadth-first

        # Some helper functions to compute left and right offsets
        lo = lambda i: 2 * i + 1
        ro = lambda i: 2 * i + 2

        # Using the fact that a binary tree stored in
        # array format is ordered in breadth-first
        # Some helper functions to compute left and right offsets
        lo = lambda i: 2 * i + 1
        ro = lambda i: 2 * i + 2
        nodes = [
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
            AVLNode(None, None),
        ]

        # Link up all the nodes in the array
        for i in range(len(nodes)):
            li = lo(i)
            if li < len(nodes):
                nodes[i].left = nodes[li]
            ri = ro(i)
            if ri < len(nodes):
                nodes[i].right = nodes[ri]

        self.assertListEqual(
            nodes,
            [x for x in BreadthFirstTraversal(nodes[0], lambda x: x)]
        )

