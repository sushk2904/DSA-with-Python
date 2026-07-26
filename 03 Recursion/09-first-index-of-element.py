def firstIndexofanElement(l1, x):
    if len(l1) == 0:
        return -1
    if l1[0] == x:
        return 0
    ansfromrecursion = firstIndexofanElement(l1[1:],x)
    if ansfromrecursion == -1:
        return ansfromrecursion
    else:
        return ansfromrecursion + 1
print(firstIndexofanElement([2,5,7,9,1,11,7,7,7], 7))

def lastIndexofanElement(l1, x):
    if len(l1) == 0:
        return -1
    ansfromrecursion1 = lastIndexofanElement(l1[1:],x)
    if ansfromrecursion1 == -1:
        return ansfromrecursion1
    else:
        return ansfromrecursion1 + 1
    if l1[0] == x:
        return 0

print(lastIndexofanElement([2,5,7,9,1,11,7,7,8], 7))