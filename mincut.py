from random import randint


def mincut(mylist):
    pass


def fuse(mylist, edge):
    pass


def select_random(mylist):
    ordered_pairs = []
    for i in range(len(mylist)):
        for j in mylist[i]:
            ordered_pairs.append((i, j))

    rand_index = randint(0, len(ordered_pairs) -1)

    return ordered_pairs[rand_index
]

def get_number_of_edges(mylist):
    a = 0
    for i in mylist:
        a += len(i)
    return a


if __name__ == "__main__":
    f = open('data\KargerMinCut.txt')
    B = []
    for line in f:
        split = line.split()
        B.append([int(x)-1 for x in split[1:-1]])

    for k in range(len(B)):
        print(str(k) + " " + str(B[k]))