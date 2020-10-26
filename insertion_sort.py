def insertionSort(xlist):
    for i in range(1, len(xlist)):
        temp = xlist[i]
        j = i - 1
        while temp < xlist[j] and j >= 0:
            xlist[j + 1] = xlist[j]
            j -= 1
        xlist[j + 1] = temp
    return xlist


if __name__ == '__main__':
    x = input('please type an array in format 1 2 5 10: ')
    xlist = x.split(' ')
    xlist = [int(xlist[i]) for i in range(len(xlist))]
    insertionSort(xlist)
    print(xlist)
