c=0
for i in range(int(input())):
    s=[int(i) for i in input().split()]
    if s[0]+2 <= s[1]:
        c+=1
print(c)
