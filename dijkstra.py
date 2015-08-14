class Tracker:
    def __init__(self, init_node):
        self.X = set()
        self.X.add(init_node)
        self.A = {init_node: 0}


class Edge:
    def __init__(self, destination, cost):
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        return "[" + str(self.destination) + "|" + str(self.cost) + "]"


if __name__ == "__main__":
    f = open('data\Dijkstra.txt')

    data = {}

    for i in f:
        split = i.split()
        data[int(split[0])] = [Edge(int(x.split(',')[0]), int(x.split(',')[1])) for x in split[1:]]

    N = len(data)

    tracker = Tracker(1)

    while len(tracker.X) < N:
        best_score = 2 ** 31
        best_source = None
        best_destination = None

        for visited_node in tracker.X:
            for edge in data[visited_node]:
                if edge.destination not in tracker.X:
                    if tracker.A[visited_node] + edge.cost < best_score:
                        best_score = tracker.A[visited_node] + edge.cost
                        best_source = visited_node
                        best_destination = edge.destination

        tracker.X.add(best_destination)
        tracker.A[best_destination] = best_score

    print(tracker.A)

    nodes = [7,37,59,82,99,115,133,165,188,197]
    print([(tracker.A[k]) for k in nodes])