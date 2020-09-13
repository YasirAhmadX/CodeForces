l=[0 for i in range(int(input()))]
s=[int(i)-1 for i in input().split()]
for n in range(len(s)):
    l[s[n]]=str(n+1)
print(' '.join(l))
