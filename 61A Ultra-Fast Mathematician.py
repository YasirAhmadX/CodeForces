x=input()
y=input()
r=''
for i in range(len(x)):
    r+=str(int(x[i])^int(y[i]))
print(r)
