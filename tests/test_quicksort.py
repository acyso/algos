import unittest
from quicksort import *


def load10():
    f = open('data/qs_test1.txt')
    output = []
    for a in f:
        output.append(int(a))
    return output


def load100():
    f = open('data/qs_test2.txt')
    output = []
    for a in f:
        output.append(int(a))
    return output


def load1000():
    f = open('data/qs_test3.txt')
    output = []
    for a in f:
        output.append(int(a))
    return output


class Tests(unittest.TestCase):

    def test_swap(self):
        A = [1, 2, 3, 4, 5]
        swap(A, 1, 2)
        self.assertSequenceEqual([1, 3, 2, 4, 5], A)

    def test_partition_left(self):
        A = [3, 8, 2, 5, 1, 4, 7, 6]
        partition_left(A, 0, 8)
        self.assertSequenceEqual([1, 2, 3, 5, 8, 4, 7, 6], A)

    def test_median(self):
        A = [4, 5, 6, 7]
        self.assertEqual((1, 5), get_median(A, 0, 4))
        B = [8, 2, 4, 5, 7, 1]
        self.assertEqual((2, 4), get_median(B, 0, 6))
        C = [1, 2, 3, 4, 6, 10, 9, 5, 7, 8]
        self.assertEqual((9, 8), get_median(C, 3, 10))

    def test_left_10(self):
        A = load10()
        q = quicksort(A, 0, 10, 'left')
        self.assertEqual(25, q)
        self.assertSequenceEqual(range(1, 11), A)

    def test_right_10(self):
        A = load10()
        q = quicksort(A, 0, 10, 'right')
        self.assertEqual(29, q)
        self.assertSequenceEqual(range(1, 11), A)

    def test_median_10(self):
        A = load10()
        q = quicksort(A, 0, 10, 'median')
        self.assertEqual(21, q)
        self.assertSequenceEqual(range(1, 11), A)

    def test_left_100(self):
        A = load100()
        q = quicksort(A, 0, 100, 'left')
        self.assertEqual(615, q)
        self.assertSequenceEqual(range(1, 101), A)

    def test_right_100(self):
        A = load100()
        q = quicksort(A, 0, 100, 'right')
        self.assertEqual(587, q)
        self.assertSequenceEqual(range(1, 101), A)

    def test_median_100(self):
        A = load100()
        q = quicksort(A, 0, 100, 'median')
        self.assertEqual(518, q)
        self.assertSequenceEqual(range(1, 101), A)

    def test_left_1000(self):
        A = load1000()
        q = quicksort(A, 0, 1000, 'left')
        self.assertEqual(10297, q)
        self.assertSequenceEqual(range(1, 1001), A)

    def test_right_1000(self):
        A = load1000()
        q = quicksort(A, 0, 1000, 'right')
        self.assertEqual(10184, q)
        self.assertSequenceEqual(range(1, 1001), A)

    def test_median_1000(self):
        A = load1000()
        q = quicksort(A, 0, 1000, 'median')
        self.assertEqual(8921, q)
        self.assertSequenceEqual(range(1, 1001), A)


if __name__ == '__main__':
    unittest.main()