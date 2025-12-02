#Armstrong number is a number which is the sum of individual digits raised to the power of total no. of digits i.e., if the number is 153, 1^3 + 5^3 + 3^3
n = 5348
num = n
nod = len(str(n))
total = 0

while num > 0:
    ld = num %10
    total = total + (ld**nod)
    num = num//10

if n == total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")