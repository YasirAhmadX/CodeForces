n,l=input().split()
n=[i for i in input()]
i=0
while i<int(l):
    j=0
    while j<len(n)-1:
        if n[j]<n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
            j+=1
        j+=1
    i+=1
print(''.join(n))
