input()
l=''.join(input().split())
if oct(int(l))=='0o0':
    print('EASY')
else:
    print('HARD')
