l=input()
l=[int(i) for i in input().split()]
max=min=l[0]
c=0
for i in l:
    if i<min:
        min=i
        c+=1
    elif i>max:
        max=i
        c+=1
print(c)
