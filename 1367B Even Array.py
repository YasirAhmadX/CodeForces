for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=x=0
    for i in range(n):
        if i%2!=l[i]%2:
            c+=1
        if l[i]%2!=0:
            x+=1
    if c%2==0 and n//2==x:
        print(c//2)
    else:
        print(-1)
