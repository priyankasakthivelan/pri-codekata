p=input()
q=len(p)
r=""
for i in range (q):
  if((i%2)==0):
    r+=p[i+1]
  else:
    r+=p[i-1]
print (r)