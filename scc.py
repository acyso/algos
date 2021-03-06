import sys
import resource

class Tracker():
    def __init__(self):
        self.current_source = None
        self.current_time = 0
        self.explored_nodes = set()
        self.leaders = {}
        self.finish_time = {}

    def reset(self):
        self.current_source = None
        self.current_time = 0
        self.explored_nodes = set()


def dfs_loop(G, nodes, tracker):
    for n in nodes:
        if n not in tracker.explored_nodes:
            tracker.current_source = n
            dfs(G, n, tracker)


def dfs(G, i, tracker):
    tracker.explored_nodes.add(i)
    tracker.leaders[i] = tracker.current_source
    if i in G:
        for h in G[i]:
            if h not in tracker.explored_nodes:
                dfs(G, h, tracker)
    tracker.current_time += 1
    tracker.finish_time[i] = tracker.current_time


if __name__ == "__main__":
    sys.setrecursionlimit(1000000)

    datafile = open('data/SCC.txt')
    #datafile = open('tests/data/scc_test2.txt')
    #datafile = open('data\SCC.txt')
    N = 0
    G = {}
    Grev = {}
    for i in datafile:
        a = [int(a)-1 for a in i.split()]

        if a[0] > N:
            N = a[0]
        if a[1] > N:
            N = a[1]

        if a[0] == a[1]:
            continue
        G.setdefault(a[0], []).append(a[1])
        Grev.setdefault(a[1], []).append(a[0])

    tracker = Tracker()
    dfs_loop(Grev, range(N-1, -1, -1), tracker)
    sorted_nodes = sorted(tracker.finish_time, key=tracker.finish_time.get, reverse=True)

    tracker.reset()
    dfs_loop(G, sorted_nodes, tracker)

    output = {}
    for k in tracker.leaders:
        v = tracker.leaders[k]
        if v in output:
            output[v] += 1
        else:
            output[v] = 1

    sorted_output = []
    for i in output:
        sorted_output.append(output[i])
   
    final = sorted(sorted_output, reverse=True)
    print(final[:min(len(final), 5)]) 

