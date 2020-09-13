n=int(input())
l=[100,20,10,5,1]
c=0
for i in l:
    if n==0:
        break
    elif i<=n:
        x=n//i
        n=n%i
        c+=x
print(c)
