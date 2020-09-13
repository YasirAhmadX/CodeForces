for i in range(int(input())):
    n=int(input())
    n=[int(i) for i in input().split()]
    print('YES' if sum(n)%2==1 else 'NO')
