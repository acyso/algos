import unittest

def quicksort(A):
    print("called quicksort with " + str(A))
    if len(A) <= 1:
        return
    pivot_index = get_pivot_index()
    partition(A, pivot_index)

    #here's the error: where does the pivot_index_value end up?
    quicksort(A[:pivot_index])
    quicksort(A[pivot_index+1:])


def get_pivot_index():
    return 0


def partition(A, index):
    if len(A) <= 1:
        return
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
    #unittest.main()
    A = [3, 8, 2, 5, 1, 4, 7, 6]
    quicksort(A)
    print(A)