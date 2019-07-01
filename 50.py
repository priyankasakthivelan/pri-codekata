n=int(input())
p=(n & n-1)
if p!= 0:
  print('no')
else:
  print('yes')