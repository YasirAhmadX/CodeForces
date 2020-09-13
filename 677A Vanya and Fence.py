f,h=[int(i) for i in input().split()]
f=[int(i) for i in input().split()]
s=0
for l in range(len(f)):
    if f[l]>h:
        s+=2
    else:
        s+=1
print(s)
