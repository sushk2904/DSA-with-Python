def Updateindexofallelementsinlist(l1, x, index, ansList):
    if len(l1) == index:
        return
    

    if l1[index] == x:
        ansList.append(index)

    Updateindexofallelementsinlist(l1,x,index+1, ansList)
    
    
ansList = []
Updateindexofallelementsinlist([3,2,5,2,8,2,1],2,0, ansList)
print(ansList)