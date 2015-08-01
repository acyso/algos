from random import randint


def mincut(mylist):
    pass


def fuse(mylist, edge):
    persisting_node = edge[0]
    disappearing_node = edge[1]
    mylist[persisting_node] += mylist[disappearing_node]
    mylist[disappearing_node] = []

    new_connections = []
    for i in mylist[persisting_node]:
        if i != persisting_node:
            new_connections.append(i)

    mylist[persisting_node] = new_connections

    print(mylist)


def get_edges(d):
    ordered_pairs = []
    for i in d:
        for j in d[i]:
            ordered_pairs.append((i, j))
    return ordered_pairs

    
def select_random_edge(edges):
    rand_index = randint(0, len(edges) - 1)
    return edges[rand_index]


def get_number_of_edges(d):
    a = 0
    for i in d:
        a += len(d[i])
    return a


if __name__ == "__main__":
    f = open('data\KargerMinCut.txt')
    B = {}
    for line in f:
        split = line.split()
        B[int(split[0])] = [int(x) for x in split[1:-1]]

    for k in range(1, len(B) + 1):
        print(str(k) + " " + str(B[k]))