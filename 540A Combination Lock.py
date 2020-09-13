n=int(input())
l=input()
p=input()
m=0
for x in range(n):
    i,j=int(l[x]),int(p[x])
    a=i-j
    if a<0:
        a=-a
    if a>5:
        m+=10-a
    else:
        m+=a
print(m)
