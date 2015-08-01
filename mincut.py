



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