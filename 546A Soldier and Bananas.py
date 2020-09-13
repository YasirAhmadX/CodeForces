k,n,w=[int(i) for i in input().split()]
x=int(n-(w/2 *(w+1)*k))
if x>0:
    print(0)
else:
    print(-x)
