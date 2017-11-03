'''
Created on Jun 9, 2016

@author: Md. Rezwanul Haque
'''
from collections import defaultdict

d, n = defaultdict(list), list(map(int, input().split()))

for i in range(n[0]):
    d[input()].append(i + 1)

for i in range(n[1]):
    print(' '.join(map(str, d[input()])) or -1)