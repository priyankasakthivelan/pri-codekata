p=int(input())
if(p<60):
    print(0,p)
else:
    h=p//60
    m=p%60
    print(h,m)
