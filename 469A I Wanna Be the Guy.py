l=int(input())
A=set([int(i) for i in input().split()][1::])
B=set([int(i) for i in input().split()][1::])
A=A.union(B)
if len(A)==l:
    print('I become the guy.')
else:
    print("Oh, my keyboard!")
