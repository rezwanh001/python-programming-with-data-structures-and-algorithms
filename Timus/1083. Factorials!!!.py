def Main():
    n, s = map(str, input().split())
    ln = len(s)
    fact = 1
    n = int(n)
    for i in range(n, 1, -ln):
        fact *= i
    print(fact)

if __name__ == '__main__':
    Main()