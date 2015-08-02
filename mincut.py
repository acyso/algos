from random import randint
import sys
import copy


def mincut(d):
    while True:
        if len(d) == 2:
            for k in d:
                return len(d[k])

        edges = get_edges(d)
        edge_to_fuse = select_random_edge(edges)
        fuse(d, edge_to_fuse)


def fuse(d, edge):
    # print("fusing " + str(d) + " " + str(edge))
    persisting_node = edge[0]
    disappearing_node = edge[1]
    source_edges = d[persisting_node]
    dest_edges = d[disappearing_node]

    source_edges = [x for x in source_edges if x != disappearing_node]
    dest_edges = [x for x in dest_edges if x != persisting_node]

    temp_persisting_edges = source_edges + dest_edges

    # remap edges
    for k in d:
        for i, v in enumerate(d[k]):
            if v == disappearing_node:
                d[k][i] = persisting_node

    d[persisting_node] = temp_persisting_edges
    d.pop(disappearing_node, None)
    # print("result " + str(d))

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
    corrvalue = sys.maxsize

    f = open('data\KargerMinCut.txt')
    #f = open('tests\data\mincut_test1.txt')
    B = {}
    for line in f:
        split = line.split()
        B[int(split[0])] = [int(x) for x in split[1:]]
    f.close()
    print(B)

    for i in range(200000):
        if i % 10 == 0:
            print('i = {}, best = {}'.format(i, corrvalue))
        C = copy.deepcopy(B)
        q = mincut(C)
        if q < corrvalue:
            corrvalue = q
    print(corrvalue)