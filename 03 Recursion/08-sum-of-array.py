def sumarray(l1, index, count):
    if len(l1) == 0 or len(l1) == index:
        return 
    if l1[index] > 0:
        count+= l1[index]
    sumarray(l1, index+1, count)

count = 0

sumarray([3,2,5,2,8,2,1],0,0)
print(count)
    