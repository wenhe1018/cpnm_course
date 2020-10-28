import math


def stirlings(n):
    return n * math.log(n) - n


if __name__ == '__main__':
    n = 5000
    print(str(math.log(math.factorial(n))) + ' | ' + str(stirlings(n)))
