s=''
n=int(input())
for i in range(1,n+1):
    if i>1:
        s=s+'that '
    if i%2!=0:
        s=s+'I hate '
    else:
        s=s+'I love '
s=s+'it'
print(s)
