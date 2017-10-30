from math import ceil
n,m,a = map(int,input().split())
A = ceil(n/a)
B = ceil(m/a)
print(int(A*B))