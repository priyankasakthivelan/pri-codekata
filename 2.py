try:
  n=5
  if(n<0):
    print("invalid")
  elif(n%2==0):
    print("it is even")
  elif(n%2!=0):
    print("it is odd")
except ValueError:
    print("invalid input")
