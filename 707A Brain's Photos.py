n,m=[int(i) for  i in input().split()]
x=set()
c={'C','M','Y'}
for i in range(n):
    l=set(input().split())
    x=x.union(l)
print("#Black&White" if x.isdisjoint(c) else "#Color")
