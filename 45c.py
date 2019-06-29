p= int(input())
counts = 0
while p > 0:
  p= p // 10
  counts = counts + 1
print(counts)