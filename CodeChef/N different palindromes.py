from string import ascii_lowercase
T = int(input())
for i in range(T):
    chars = ascii_lowercase
    n = int(input())
    ans = ''
    ind = 0
    while ind<n:
        ans += chars[ind%26]
        ind += 1
    print (ans)