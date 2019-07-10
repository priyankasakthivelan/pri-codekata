a=int(input())
f=0
for r in range(1,a):
  if a%r==0:
    f=r
if f>1:
  print('yes')
#elif a==1:
 # print 'The number 1 is neither prime nor composite!'
else:
  print('no')