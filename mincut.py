from random import randint


def mincut(mylist):
    pass


def fuse(d, edge):
    persisting_node = edge[0]
    disappearing_node = edge[1]
    source_edges = d[persisting_node]
    dest_edges = d[disappearing_node]

    source_edges.remove(disappearing_node)
    dest_edges.remove(persisting_node)

    temp_persisting_edges = source_edges + dest_edges
    temp_persisting_edges = [x for x in temp_persisting_edges if x != persisting_node]

    for k in d:
        for i, v in enumerate(d[k]):
            if v == disappearing_node:
                d[k][i] = persisting_node

    d[persisting_node] = temp_persisting_edges
    d.pop(disappearing_node, None)


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