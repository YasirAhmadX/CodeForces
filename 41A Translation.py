ss=input()
rs=input()
for i in range(len(ss)+1 //2):
    if ss[i]!=rs[-(i+1)]:
        print('NO')
        exit()
print('YES')
