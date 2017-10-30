def Main():
    while True:
        H1, M1, H2, M2 = map(int, input().split())
        if H1 == M1 == H2 == M2 == 0:
            break
        else:
            x = H1 * 60 + M1
            y = H2 * 60 + M2

            if (y <= x):
                y += 24 * 60

            print(abs(y - x))


if __name__ == '__main__':
    Main()