L,B=input().split()
L,B=int(L),int(B)
c=0
while L<=B:
    L*=3
    B*=2
    c+=1
print(c)
