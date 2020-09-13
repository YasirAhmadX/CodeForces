x=0
p=''
for i in range(int(input())):
    s=input()
    if s==p:
        continue
    else:
        x+=1
        p=s
print(x)
