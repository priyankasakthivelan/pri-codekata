try:
  n=5
  if(n<0):
    print("invalid")
  elif(n%2==0):
    print("even")
  elif(n%2!=0):
    print("odd")
except ValueError:
    print("invalid")
