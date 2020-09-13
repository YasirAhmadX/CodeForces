for _ in range(int(input())):
    a,b=[int(i) for i in input().split()]
    mn=min(a,b)
    mx=a+b - mn #max(a,b)
    i=1
    while True:  # Since limits are small:Just use brute force
        if ((i**2) >= 2*a*b) and (i>=2*mn) and (i>=mx):
            print(i**2)
            break
        i+=1
