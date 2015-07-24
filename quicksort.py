def quicksort(A, i, j, method):
    if len(A) <= 1:
        return

    if method == 'left':
        correct_pivot_index = partition_left(A, i, j)
    elif method == 'right':
        correct_pivot_index = partition_right(A, i, j)

    N = j - i - 1

    if correct_pivot_index - i >= 1:
        N += quicksort(A, i, correct_pivot_index, method)
    if j - correct_pivot_index - 1 >= 1:
        N += quicksort(A, correct_pivot_index + 1, j, method)

    return N

def partition_left(A, left, right):
    pivot = A[left] #modify this!
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

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


if __name__ == '__main__':
    A = [3, 8, 2, 5, 1, 4, 7, 6]
    print(quicksort(A, 0, 8, 'left'))
    print(A)