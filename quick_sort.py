def quickSort(xlist, left, right):
    if left < right:
        pivot = partition(xlist, left, right)
        quickSort(xlist, left, pivot - 1)
        quickSort(xlist, pivot + 1, right)


def partition(xlist, left, right):
    pivot = xlist[right]
    while left < right:
        while left < right and xlist[left] <= pivot:
            left += 1
        xlist[right] = xlist[left]
        while left < right and xlist[right] >= pivot:
            right -= 1
        xlist[left] = xlist[right]
    xlist[left] = pivot
    return left


if __name__ == '__main__':
    x = input('please type an array in format 1 2 5 10: ')
    xlist = x.split(' ')
    xlist = [int(xlist[i]) for i in range(len(xlist))]
    quickSort(xlist, 0, len(xlist) - 1)
    print(xlist)
