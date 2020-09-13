l=[]
for _ in range(int(input())):
    l.append(input())
for s in l:
    if len(s)>10:
        print(s[0],len(s)-2,s[-1],sep='')
    else:
        print(s)
