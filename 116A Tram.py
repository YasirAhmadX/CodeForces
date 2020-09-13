mP=0 #max Population
P=0
for _ in range(int(input())):
    W=[int(i) for i in input().split()]
    P=P+(W[1]-W[0])
    if P>mP:
        mP=P
print(mP)
