n,k=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]
nTm=0 #NumberOfTeamMembers
for i in l:
    if i+k<=5:
        nTm+=1
print(nTm//3)
