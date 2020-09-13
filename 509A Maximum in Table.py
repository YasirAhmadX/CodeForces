n=int(input())
l=[1 for i in range(n)]
for i in range(1,n):
    for x in range(n):
        if x==0:
            continue
        else:
            l[x]=l[x]+l[x-1]

print(l[-1])
