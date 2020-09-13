n=int(input())
c=0
for q in range(1,n//2 +1):
    m=(n-q)/q
    if m>=1 and m%1==0:
        c+=1
print(c)
