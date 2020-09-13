n=int(input())
w=[int(i) for i in input().split()]
ex=0 #expenditure
m=max(w)
for i in w:
    ex+=(m-i)
print(ex)
