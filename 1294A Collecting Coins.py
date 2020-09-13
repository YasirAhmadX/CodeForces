for _ in range(int(input())):
    a,b,c,n=[int(i) for  i in input().split()]
    x=max(a,b,c)
    n=n-(3*x - (a+b+c))
    print('YES' if n%3==0 else 'NO')
