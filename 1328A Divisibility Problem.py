for _ in range(int(input())):
    a,b=[int(i) for i in input().split()]
    print(b-(a%b) if a%b!=0 else 0)
