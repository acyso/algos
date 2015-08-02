import unittest
from mincut import *


class Tests(unittest.TestCase):

    def test_get_number_of_edges(self):
        A = {1: [1, 2], 2: [1, 3, 4], 3: [1]}
        out = get_number_of_edges(A)
        self.assertEqual(6, out)

    def test_get_edges(self):
        A = {1: [1, 2], 2: [1, 3, 4], 3: [1]}
        out = get_edges(A)
        self.assertEqual(6, len(out))
        self.assertTrue((1, 1) in out)
        self.assertTrue((1, 2) in out)
        self.assertTrue((2, 1) in out)
        self.assertTrue((2, 3) in out)
        self.assertTrue((2, 4) in out)
        self.assertTrue((3, 1) in out)

    def test_fuse(self):
        A = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
        fuse(A, (1, 3))
        self.assertSequenceEqual([2, 2, 4], A[1])
        self.assertSequenceEqual([1, 1, 4], A[2])
        self.assertSequenceEqual([2, 1], A[4])
        self.assertEqual(3, len(A))
        self.assertFalse(3 in A)