def isBeautiful(n):
    x=set()
    for i in str(n):
        x.add(i)
    return len(x)==4
s=int(input())
while True: #Get Ready for Some BruteForc Action
#Atmost next beautiful year will be 30-50 years later(eyeballed it)
#So bruteforce will be enough for this
    s+=1
    if isBeautiful(s):
        print(s)
        exit()
