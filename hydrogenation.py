def rate(conc):
    k = 4e5
    h_conc = 1
    rates = []
    for c in range(21):
        rates.append(round(((k * h_conc * conc) / ((1 + c * conc)**2)), 2))
    return rates


if __name__ == '__main__':
    for conc in range(10):
        print(str(rate(conc)))
