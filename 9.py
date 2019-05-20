try:
	number=list()
	p1,c1 = input().split()
	c1 = int(c1)
	p1 = int(p1)
	add = 0
	number=input().split()
	for iter in range(0,c1):
	    add = add + int(number[iter])
	print (add)
except ValueError:
	print("invalid")
