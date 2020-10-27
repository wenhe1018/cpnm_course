def constant(fn, x1, x2, n):
    deltax = (x2 - x1) / float(n)
    area = 0.0
    for i in (range(n)):
        x_left = x1 + float(i) * deltax
        f1 = fn(x_left)
        area = area + f1 * deltax
    return area


def trapezium(fn, x1, x2, n):
    deltax = (x2 - x1) / float(n)
    area = 0.0
    for i in (range(n)):
        x_left = x1 + float(i) * deltax
        x_right = x1 + float(i + 1) * deltax
        f1 = fn(x_left)
        f2 = fn(x_right)
        area = area + (f1 + f2) * deltax * 0.5
    return area


def midpoint(fn, x1, x2, n):
    deltax = (x2 - x1) / float(n)
    area = 0.0
    for i in (range(n)):
        x_mid = x1 + float(i + 0.5) * deltax
        f_mid = fn(x_mid)
        area = area + (f_mid) * deltax
    return area


def simpsons(fn, x1, x2, n):
    deltax = (x2 - x1) / (2 * float(n))
    sum = 0.0
    for i in (range(n)):
        f1 = fn(x1 + 2 * i * deltax)
        f2 = 4 * fn(x1 + (2 * i + 1) * deltax)
        f3 = fn(x1 + 2 * (i + 1) * deltax)
        sum = sum + f1 + f2 + f3
    area = sum * deltax / 3
    return area


def fn(x):
    return x**2


if __name__ == '__main__':
    n = 200
    print(constant(fn, 0, 10, n))
    print(trapezium(fn, 0, 10, n))
    print(midpoint(fn, 0, 10, n))
    print(simpsons(fn, 0, 10, n))
