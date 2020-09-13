a,b=[int(i) for i in input().split()]
n=1
while True:
    x=a*n
    if (x-b)%10 == 0 or (x)%10==0:
        print(n)
        exit()
    n+=1
