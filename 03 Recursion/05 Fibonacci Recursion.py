def FibSer(FibSum,i, n):
    if i<=n:
        print(FibSum)
    FibSer(FibSum+i,i+n,n-1)

FibSer(0,0,5)

      
    


