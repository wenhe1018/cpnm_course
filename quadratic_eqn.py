def calc_roots(a, b, c):
    discriminant = b**2 - 4.0 * a * c
    if discriminant < 0:
        print('discriminant is negative')
        return
    elif discriminant == 0:
        print('discriminant = 0, two roots are same value')
        return [(-b) / (2 * a)]
    else:
        root1 = (-b + (discriminant)**(1/2)) / (2 * a)
        root2 = (-b - (discriminant)**(1/2)) / (2 * a)
        return [root1, root2]


if __name__ == '__main__':
    a = input('please give a: ')
    b = input('please give b: ')
    c = input('please give c: ')
    print(calc_roots(int(a), int(b), int(c)))
