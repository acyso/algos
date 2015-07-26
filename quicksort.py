from math import floor
from statistics import median

def quicksort(A, i, j, method):
    if len(A) <= 1:
        return

    if method == 'left':
        correct_pivot_index = partition_left(A, i, j)
    elif method == 'right':
        correct_pivot_index = partition_right(A, i, j)
    elif method == 'median':
        correct_pivot_index = partition_median(A, i, j)
    else:
        raise Exception("invalid method")

    N = j - i - 1

    if correct_pivot_index - i >= 1:
        N += quicksort(A, i, correct_pivot_index, method)
    if j - correct_pivot_index - 1 >= 1:
        N += quicksort(A, correct_pivot_index + 1, j, method)

    return N


def partition_left(A, left, right):
    pivot = A[left]
    i = left + 1
    for j in range(left+1, right):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    swap(A, left, i - 1)
    return i - 1


def partition_right(A, left, right):
    swap(A, right-1, left)
    pivot = A[left]
    i = left + 1
    for j in range(left+1, right):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    swap(A, left, i - 1)
    return i - 1


def partition_median(A, left, right):
    #print("calling with " + str(A) + " " + str(left) + " " + str(right))
    pivot_index, pivot_value = get_median(A, left, right)
    swap(A, pivot_index, left)
    pivot = A[left]
    i = left + 1
    for j in range(left+1, right):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    swap(A, left, i - 1)
    return i - 1


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def get_median(A, left, right):
    midindex = floor((right+left-1)/2)
    middle = A[midindex]
    first = A[left]
    last = A[right-1]
    out = median([first, middle, last])
    if out == first:
        return left, out
    elif out == last:
        return right-1, out
    else:
        return midindex, out


if __name__ == '__main__':
    A = [3, 8, 2, 5, 1, 4, 7, 6]
    print(quicksort(A, 0, 8, 'left'))
    print(A)

    f = open('data\QuickSort.txt')
    B = []
    C = []
    D = []
    for i in f:
        B.append(int(i))
        C.append(int(i))
        D.append(int(i))

    left = quicksort(B, 0, len(B), 'left')
    print(str(left))
    right = quicksort(C, 0, len(C), 'right')
    print(str(right))
    med = quicksort(D, 0, len(D), 'median')
    print(str(med))