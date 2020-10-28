def fibo_recur(n):
    if n <= 1:
        return 1
    else:
        return fibo_recur(n - 2) + fibo_recur(n - 1)


if __name__ == '__main__':
    series = []
    for i in range(25):
        series.append(fibo_recur(i))
    print(series)
