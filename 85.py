p=list(input())
if len(p)%2==0:
    p[int(len(p)/2)]='*'
    p[int(len(p)/2)-1]='*'
else:
    p[int(len(p)/2)]='*'
for i in range(len(p)):
    print(p[i],end='')