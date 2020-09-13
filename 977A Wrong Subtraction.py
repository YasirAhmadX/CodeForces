N,n=[int(i) for i in input().split()]
for i in range(n):
    if N%10==0:
        N//=10
    else:
        N-=1
print(N)
