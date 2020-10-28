import argparse


def vdw(a, b, t, v, n):
    # here we take gas const with unit of m**3·Pa·K**−1·mol**−1
    r = 8.3144598
    p1 = (n * r * t) / (v - n * b)
    p2 = ((n**2) * a) / (v**2)
    return p1 - p2


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=float)
    parser.add_argument('-b', type=float)
    parser.add_argument('-t', type=float)
    parser.add_argument('-v1', type=float)
    parser.add_argument('-v2', type=float)
    parser.add_argument('-n', type=float)
    args = parser.parse_args()
    v = [args.v1 + (i * (args.v2 - args.v1) / 10) for i in range(10)]
    for volume in range(len(v)):
        print(vdw(args.a, args.b, args.t, v[volume], args.n))
