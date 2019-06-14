p=int(input())
q=[]
for i in range(p):
    q.append(input())
r=q[0]
s,a=0,0
n=""
for i in range(len(r)):
    a=0
    for k in range(1,p):
          if r[i]==q[k][i]:
            a=a+1
    if a==p-1:
       n=n+r[i]
    else:
        break
print(n)