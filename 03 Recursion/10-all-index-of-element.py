"""def printallindexofelement(l1,x,index):
    if len(l1) == index:
        return
    if l1[index] == x:
        print(index)

    return printallindexofelement(l1, x, index+1)

printallindexofelement([1,4,1,6,4,7,9], 1, 0)"""


"""def printallindexofelementhelper(l1,x,index):
    if len(l1) == index:
        return
    return printallindexofelementhelper(l1, x, index+1)

    if (l1[index]==x):
        print(index)


def printallindexofelement(l1,x):
    #helper function
    printallindexofelementhelper(l1,x,0)

printallindexofelement([1,4,1,6,4,7,9], 1)"""