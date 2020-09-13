m,n=[int(i) for i in input().split()]
left=1
for i in range(m):
    if i%2==0:
        print(n*'#')
        left= not left
    else:
        if left:
            x= '#'+'.'*(n-1)
        else:
            x='.'*(n-1) + '#'
        print(x)
