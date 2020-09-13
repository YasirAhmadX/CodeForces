l,a=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]
c=0
a=l[a-1]
for i in l:
    if i>=a and i>0:
        c+=1
print(c)
