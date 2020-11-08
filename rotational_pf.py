import math


def rpf_diatomic(B, T):
    kb = 1.38066e-23
    bj = B * 1.986e-23
    sum = 0
    for j in range(10000):
        exp = -(bj * j * (j + 1)) / (kb * T)
        second = math.e**exp
        first = 2 * j + 1
        whole = first * second
        sum += whole
    return round(sum, 4)


def classical(B, T):
    bj = B * 1.986e-23
    kb = 1.38066e-23
    result = T / (bj / kb)
    return round(result, 4)


if __name__ == '__main__':
    print('HCL' + '\t' + 'T' + '\t' + 'pf' + '\t' + 'classical')
    for temp in range(5, 156, 10):
        print('\t' + str(temp) + '\t' + str(rpf_diatomic(15.2, temp)) + '\t' +
              str(classical(15.2, temp)))

    print('H2' + '\t' + 'T' + '\t' + 'pf' + '\t' + 'classical')
    for temp in range(5, 156, 10):
        print('\t' + str(temp) + '\t' + str(rpf_diatomic(85.4, temp)) + '\t' +
              str(classical(85.4, temp)))

    print('NO' + '\t' + 'T' + '\t' + 'pf' + '\t' + 'classical')
    for temp in range(5, 156, 10):
        print('\t' + str(temp) + '\t' + str(rpf_diatomic(2.9, temp)) + '\t' +
              str(classical(2.9, temp)))
