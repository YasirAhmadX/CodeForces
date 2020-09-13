l=[int(input()) for i in range(5)]
d=0
for i in range(l[-1]):
    if (i+1)%l[0]==0 or (i+1)%l[1]==0 or (i+1)%l[2]==0 or (i+1)%l[3]==0:
        d+=1
print(d)
