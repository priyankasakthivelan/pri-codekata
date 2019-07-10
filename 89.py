p1,p2=map(int,input().split())
p3=p1*p2
for i in range(0,p3+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")