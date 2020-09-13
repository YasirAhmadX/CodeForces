l,j,k=[list(input()) for i in range(3)]
l.extend(j)
for i in l:
    if i not in k :
        k.append(i)
        break
    k.remove(i)
print('YES' if k==[] else 'NO')
