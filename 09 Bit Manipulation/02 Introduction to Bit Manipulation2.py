#Swap Two Numbers
a = 10
b = 5

a = a ^ b
b = a ^ b
a = a ^ b

print("a is now", a)
print("b is now", b)






#Check if ith bit is set or not
n = 13
i = 1
if (n & (i<<i)) != 0:
    print("True")
else:
    print("False")