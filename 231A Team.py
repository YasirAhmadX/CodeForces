c=0
for _ in range(int(input())):
    s=input()
    if s.count('1')>1:
        c+=1
print(c)
