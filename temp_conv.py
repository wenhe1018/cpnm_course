def c2f(temp_c):
    return round(9.0 / 5.0 * temp_c + 32, 1)


if __name__ == '__main__':
    for i in range(0, 101):
        print(str(i) + 'C | ' + str(c2f(i)) + 'F')
