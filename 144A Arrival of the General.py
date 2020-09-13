n=int(input())
x=[int(i) for i in input().split()]
Mx=Mn=0 #index of max no. & min no.
for i in range(n):
    if x[Mx]<x[i]:
        Mx=i
    if x[Mn]>=x[i]:
        Mn=i
n=(Mx)+(n-(Mn+1))
if Mx>Mn:
    n-=1
print(n)
