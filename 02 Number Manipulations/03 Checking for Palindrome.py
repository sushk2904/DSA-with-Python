n = 1234
n1 = 4321
num =n
result = 0
while num > 0:
    ld = num % 10
    result = (result*10) + ld
    num = num//10
if n1 == result:
    print("The result is palindrome")
else:
    print("The result is not palindrome")