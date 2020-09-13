s=input()
p=0
for l in s:
    if 64<ord(l)<91:
        p+=1
    else:
        p-=1
#if p=+ve; n({A,B,..,Y,Z})>n({a,b,..y,z})
#if p=-ve; n({A,B,...Y,Z})<n({a,b,..y,z})
#if p=0;  n({A,B,..,Y,Z})==n({a,b,..y,z})

if p>0:
    print(s.upper())
else:
    print(s.lower())
