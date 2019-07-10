p,q=list(map(str,input().split()))
r=len(p)
s=0
for i in range(r):
    if(p[i]!=q[i]):
        s+=1
if(s==1):
    print("yes")
else:
    print("no")