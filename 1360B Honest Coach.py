for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    l.sort()
    min=l[1]-l[0]
    for i in range(1,n):
        if l[i]-l[i-1]<= min:
            min=l[i]-l[i-1]
    print(min)
