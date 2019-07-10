p,q=map(int,input().split())
r=0
for i in range(p,q+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            r+=1
print(r)