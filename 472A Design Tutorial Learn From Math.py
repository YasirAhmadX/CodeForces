def isPrime(n):
    Prime=True
    i=2
    while i<=n**(0.5) and Prime:
        Prime=bool(n%i)
        i+=1
        if i>3:
            i+=1
    return Prime
x=int(input())
for b in range(4,x//2+1,2):
    a=x-b
    if not isPrime(a):
        print(a,b)
        exit()
