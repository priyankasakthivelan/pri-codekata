n=int(input())
m=0
i=0
while(n>0):
    i=n%10
    m=m+i
    n=n//10
print(m)