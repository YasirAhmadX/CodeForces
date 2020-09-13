for _ in range(int(input())):
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    while k>0:
        if min(a) < max(b):
            a[a.index(min(a))],b[b.index(max(b))]=b[b.index(max(b))],a[a.index(min(a))]
        k-=1
    print(sum(a))
