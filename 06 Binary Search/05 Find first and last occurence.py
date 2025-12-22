#Brute Force
nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
n = len(nums)
first = -1
last = -1
target = 3

for i in range(0,n):
    if nums[i]==target:
        if first == -1:
            first = i
        last = i
    

print("first occurence",first, "last occurence", last)
    