x=('4','7')
s=input()
s=str(s.count('4')+s.count('7'))
for i in s:
    if i not in x:
        print('NO')
        exit()
print('YES')
