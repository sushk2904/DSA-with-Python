def checkSorted(l1):
    if (len(l1)) == 0 or len(l1) == 1:
        return True
    ans = checkSorted(l1[1:])
    if l1[0] < l1[1]:
        return ans
    else:
        return False
print(checkSorted([3,55,7,11,39]))