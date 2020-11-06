def red(frequency):
    rh = 109737.32
    n2 = 1
    while True:
        for n1 in range(1, n2):
            if frequency < (rh * ((1 / n1**2.0) -
                                  (1 / n2**2.0)) + 0.1) and frequency > (rh * (
                                      (1 / n1**2.0) - (1 / n2**2.0)) - 0.1):
                return [n1, n2]
        n2 += 1


if __name__ == '__main__':
    frequencies = [9953.50, 5503.80, 1341.23, 359.87]
    ns = []
    for frequency in frequencies:
        print(str(red(frequency)))
        ns.append(red(frequency))
    single_n1 = True
    single_n2 = True
    n1 = ns[1][0]
    n2 = ns[1][1]
    for n in ns:
        if n[0] != n1:
            single_n1 = False
        if n[1] != n2:
            single_n2 = False
    if single_n1 is True or single_n2 is True:
        print("single series")
    else:
        print("not single series")
