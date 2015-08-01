import unittest
from mincut import *

class Tests(unittest.TestCase):

    def test_swap(self):
        A = [[1, 2], [1, 3, 4], [1]]
        out = get_number_of_edges(A)
        self.assertEqual(6, out)