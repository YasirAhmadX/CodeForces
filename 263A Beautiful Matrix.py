Y,X=0,0
for y in range(-2,3):
    s=input().split()
    if '1' in s:
        X=s.index('1')-2
        Y=y
print(int(((X**2)**0.5)+(Y**2)**0.5))
