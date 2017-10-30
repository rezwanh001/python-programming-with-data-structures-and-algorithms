n = int(input())
if n <= 0:
    n = -n
    sm = n*(n+1) // 2
    sm = -sm + 1
    print(sm)
else:
    sm = n*(n+1) // 2
    print(sm)