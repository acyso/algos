

if __name__ == "__main__":
    f = open('data\KargerMinCut.txt')
    B = {}
    for line in f:
        split = line.split()
        B[int(split[0])] = [int(x) for x in split[1:-1]]

    for k in B:
        print(str(k) + " " + str(B[k]))