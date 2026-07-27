def FibSer(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return FibSer(n-1) + FibSer(n-2)

print(FibSer(6))

      
    


