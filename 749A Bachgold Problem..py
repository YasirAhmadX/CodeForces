n=int(input())
print(n//2)
if n%2 == 0:

    print((n//2*'2 ').rstrip())
else:
    print((n//2 -1)*'2 ','3',sep='')
