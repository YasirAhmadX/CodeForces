n=int(input())
r=m=1
while True:
    if ((r+1)*(r+2))//2 +m <= n:
        r+=1
        m+=(r*(r+1))/2
    else:
         print(r)
         exit()
