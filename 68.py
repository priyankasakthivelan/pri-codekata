p,b=map(int,input().split())
n=list(map(int,input().split()))
for i in n:
 if(i==b):
  print("yes")
  break
else:
 print("no")