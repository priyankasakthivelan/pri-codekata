p=input()
for i in range(0,len(p)):
   if(p[i].isalpha() and p[i].isdigit()):
    print("No")
else:
  print("Yes")