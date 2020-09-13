n=int(input())
l=[i for i in input().split()]
p=[i+1 for i in range(n) if l[i]=='1']
m=[i+1 for i in range(n) if l[i]=='2']
s=[i+1 for i in range(n) if l[i]=='3']

w=min(map(len,[p,m,s]))
print(w)
for i in range(w):
    print(p[i],m[i],s[i])
