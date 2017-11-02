N, Q = map(int, input("").split())
mylist = list(map(int, input("").split()))
lmin = min(mylist)
lmax = max(mylist)
for i in range(0,Q):
        q = int(input(""))
        if (lmin > q) or (lmax  < q) :
                print ("No")
        else:
                print ("Yes")