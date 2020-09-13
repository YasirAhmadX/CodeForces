for _ in range(int(input())):
    n=int(input())
    if n%4!=0:
        print('NO')
    else:
        print('YES')
        n=n//2
        l=[2*i for i in range(1,(n)+1)]
        s=0 #stabilizer
        for i in range(n):
            if l[i]==l[n-1]:
                l.append(l[n-1]+s)
            else:
                l.append(l[i]-1)
                s+=1
        for i in l:
            print(i,end=' ')
        print()
