for _  in range(int(input())):
    n=int(input())
    L=[2**(i+1) for i in range(n)] #I want an extra 1 @l[0] to make it less
    w=[0,0]
    L=[2**(i+1) for i in range(n)]
    L[n//2 -1],L[-1]=L[-1],L[n//2 -1]
    for i in range(n):
        if i<(n//2):
            w[0]+=L[i]
        else:
            w[1]+=L[i]
    print(w[0]-w[1])
    #Algorithm is based on following idea of rearranging
    '''
    print(l)
    for i in range(0,n//2-1):
        l[i],l[i+(n//2)]=l[i+(n//2)],l[i]
        print(l)
    print(l)
    '''
