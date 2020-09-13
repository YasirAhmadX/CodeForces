input()
z=[0,0,0,0] #[z,e,r,o]
o=0
s=input()
for i in s:
    if i=='z':
       z[0]+=1
    elif i=='e':
        z[1]+=1
    elif i=='r':
        z[2]+=1
    elif i=='o':
        z[3]+=1
    else:
        o+=1
if o>=min(z):
    print((max(z)-min(z))*'1 ',end='')
    print(min(z)*'0 ')
else:
    print('0')
