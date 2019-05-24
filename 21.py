def sumOfAP( a, d,n) : 
    sum = 0
    i = 0
    while i < n : 
        sum = sum + a 
        a = a + d 
        i = i + 1
    return sum
n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
print (sumOfAP(a, d, n)) 