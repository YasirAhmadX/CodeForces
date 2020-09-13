x,t=[int(i) for i in input().split()]
t=240-t
n=0
while 2*t/5>=(n**2)+n:
    n+=1
n-=1
print(min(n,x))


'''
36>=n(2a+(n-1)d)
36>=n(10+(n-1)5)
36>=n(10+5n-5)
36>=n(5n+5)
36>=5n^2 + 5 n
2t>=5n^2 +5n
2t/5>=n^2+n

'''
