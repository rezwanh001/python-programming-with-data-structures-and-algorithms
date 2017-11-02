import functools
import sys
input = lambda: sys.stdin.readline()


@functools.lru_cache(maxsize=10000)
def Main():
    N, A, B = map(int, input().split())
    Arr = list(map(int, input().split()))
    sm = 0
    for i in range(0, len(Arr) - 1):
        zemi = abs(Arr[i] - Arr[i + 1])
        # print(zemi)
        sm += min((zemi * A), B)

    print(sm)


if __name__ == '__main__':
    Main()