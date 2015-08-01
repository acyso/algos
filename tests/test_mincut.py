import unittest
from mincut import *


class Tests(unittest.TestCase):

    def test_get_number_of_edges(self):
        A = {1: [1, 2], 2: [1, 3, 4], 3: [1]}
        out = get_number_of_edges(A)
        self.assertEqual(6, out)
