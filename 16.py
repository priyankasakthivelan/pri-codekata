x,y=input().split()
a=int(x)
b=int(y)
for i in range(a+1, b): 
   if i > 1: 
       for n in range(2, i): 
           if (i % n) == 0: 
               break
       else: 
           print(i, end=" ") 