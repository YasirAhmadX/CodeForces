for _ in range(int(input())):
    n=int(input())
    if n>=4:
        if n%2==0:
            print(0)
        else:
            print(1)
    else:
        print(4-n)
