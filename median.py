from bisect import insort_left

def get_data(filename):
    data_file = open(filename)
    for line in data_file:
        yield int(line)


if __name__ == "__main__":
    file = 'data/Median.txt'

    mydata = []
    counter = 0

    for i in get_data(file):
        insort_left(mydata, i)
        counter += mydata[(len(mydata) - 1)//2]

    print(counter)