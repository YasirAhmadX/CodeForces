hc=[]
gc=[]
c=0
for _ in range(int(input())):
    h,g=input().split()
    hc.append(h)
    gc.append(g)
for g in gc:
    c+=hc.count(g)
print(c)
