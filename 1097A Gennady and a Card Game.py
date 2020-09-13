c=input()
l=input().split()
P='NO'
for i in l:
    if i[0]==c[0] or i[1]==c[1]:
        P='YES'
        break
print(P)
