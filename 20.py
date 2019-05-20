n = int(input())
def multiple(m, n): 
  a = range(n, (m * n)+1, n) 
  print(*a)   
m = 5
multiple(m, n) 