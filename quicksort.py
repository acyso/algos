import unittest


def partition(A, index):
    pivot = A[index]
    i = index + 1
    for j in range(i, len(A)):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    swap(A, index, i - 1)


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


class Tests(unittest.TestCase):

    def test_swap(self):
        A = [1, 2, 3, 4, 5]
        swap(A, 1, 2)
        self.assertSequenceEqual([1, 3, 2, 4, 5], A)

    def test_partition(self):
        A = [3, 8, 2, 5, 1, 4, 7, 6]
        partition(A, 0)
        self.assertSequenceEqual([1, 2, 3, 5, 8, 4, 7, 6], A)

if __name__ == '__main__':
    unittest.main()