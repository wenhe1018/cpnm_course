def calc_num(molecule_mass):
    mc = 12.0038
    mn = 14.0075
    mo = 16.0000
    mh = 1.0081
    vc = 4
    vh = -1
    vn = 3
    vo = -2
    a = 0
    b = 0
    c = 0
    d = 0
    abcd = []
    while a < 10:
        while b < 10:
            while c < 20:
                while d < 10:
                    if mc * a + mn * b + mh * c + mo * d < molecule_mass + 0.05 and mc * a + mn * b + mh * c + mo * d > molecule_mass - 0.05 and vc * a + vn * b + vh * c + vo * d == 0:
                        abcd.append([a, b, c, d])
                    d += 1
                c += 1
                d = 0
            b += 1
            c = 0
        a += 1
        b = 0
    return abcd


if __name__ == '__main__':
    print(str(calc_num(103.08)))
    print(str(calc_num(152.11)))
    print(str(calc_num(152.10)))
    print(str(calc_num(153.09)))
