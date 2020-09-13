def F(s1,s2):
    for i,j in zip(s1,s2):
        if i>j:
            return 1
        elif i<j:
            return -1
    return 0

print(F(input().lower(),input().lower()))
