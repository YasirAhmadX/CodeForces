n=int(input())
e=[int(i) for i in input().split()]
ap=0 #Available Police
uc=0 #Unchecked Case
for i in e:
    if i>0:
        ap+=i
    else:
        x= ap+i #since i is negative ap+i=ap-|i|
        if x>0:
            ap=x
        else:
            ap=0
            uc+=(-x)
print(uc)
