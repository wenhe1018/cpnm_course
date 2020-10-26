def bubbleSort(xlist):
    for num in range(len(xlist)-1, 0, -1):
        for i in range(num):
            if xlist[i] > xlist[i+1]:
                temp = xlist[i]
                xlist[i] = xlist[i+1]
                xlist[i+1] = temp
    return xlist


if __name__ == '__main__':
    x = input('please type an array in format 1 2 5 10: ')
    xlist = x.split(' ')
    xlist = [int(xlist[i]) for i in range(len(xlist))]
    bubbleSort(xlist)
    print(xlist)
