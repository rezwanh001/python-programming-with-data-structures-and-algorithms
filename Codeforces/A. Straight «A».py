def Main():
    n, k = map(int, input().split())
    sm = 0
    arr = list(map(int, input().split()))
    sm = sum(arr)
    N = n
    cnt = 0
    while (sm + N // 2) // N < k:
        sm += k
        N += 1
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    Main()