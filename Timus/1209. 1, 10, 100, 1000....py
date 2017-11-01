import  math
T = int(input())
while T != 0:
    k = int(input())
    t = int(math.sqrt((k-1)*2))

    if (t*(t+1)//2 + 1) == k:
        print(1, end=' ')
    else:
        print(0, end=' ')

    T -= 1

# Vertict TLE