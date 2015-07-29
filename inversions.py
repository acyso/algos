from math import floor


def count(a):
    n = len(a)
    if n <= 1:
        return 0, a
    if n == 2:
        if a[1] < a[0]:
            return 1, a[::-1]
        return 0, a
    else:
        cut = floor(n/2)
        inv1, a1 = count(a[:cut])
        inv2, a2 = count(a[cut:])
        xinv, a = merge(a1, a2)
        return inv1 + inv2 + xinv, a


def merge(res1, res2):
    i, j = 0, 0
    invs = 0
    out = [0] * (len(res1)+len(res2))
    for k in range(len(res1)+len(res2)):
        if (i < len(res1)) and (j < len(res2)):
            if res1[i] < res2[j]:
                out[k] = res1[i]
                i += 1
            else:
                out[k] = res2[j]
                j += 1
                invs += len(res1) - i
        elif (i >= len(res1)):
            out[k] = res2[j]
            j+=1
        elif (j >= len(res2)):
            out[k] = res1[i]
            i+=1
    return invs, out


if __name__ == "__main__":
    A = [5, 1, 2, 3, 0 ,4]
    print(count(A))

    f = open('data\IntegerArray.txt')
    B = []
    for i in f:
        B.append(int(i))
    print(count(B))