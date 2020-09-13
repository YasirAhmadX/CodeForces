w=0
for _ in range(int(input())):
    M,C=[int(i) for i in input().split()]
    if M>C:
        w+=1
    elif M<C:
        w-=1
if w==0:
    print('Friendship is magic!^^')
elif w>0:
    print('Mishka')
else:
    print('Chris')
