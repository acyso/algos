
def algo1(raw, N, M):
    out = 0
    for i in range(N, M):
        if (i % 10 == 0):
            print(i)
        for k in raw:
            if i - k in raw:
                if i - k != k:
                    out += 1
                    break
    return out


if __name__ == "__main__":
    datafile = open('data/sum.txt')

    raw = []
    for line in datafile:
        raw.append(int(line))

    print(algo1(frozenset(raw), -10000, 10001))
    #print(algo1([-2, 2, 3, 4, 5], -5, 6))
