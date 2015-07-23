def quicksort(A, i, j):
    if len(A) <= 1:
        return
    correct_pivot_index = partition(A, i, j)

    N = j - i - 1

    if correct_pivot_index - i >= 1:
        N += quicksort(A, i, correct_pivot_index)
    if j - correct_pivot_index - 1 >= 1:
        N += quicksort(A, correct_pivot_index + 1, j)

    return N

def partition(A, left, right):
    pivot = A[left] #modify this!
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
    print(quicksort(A, 0, 8))
    print(A)