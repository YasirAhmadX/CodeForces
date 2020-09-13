l=[int(input()) for _ in range(int(input()))]
for n in l:
    r=0
    for i in str(n):
        if i!='0':
            r+=1
    print(r)
    r=0
    while n>0:
        if n%10!=0:
            print((n%10)*10**r,end=' ')
        r+=1
        n=n//10
    print()
