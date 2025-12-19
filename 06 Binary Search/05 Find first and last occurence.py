#Brute Force
nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
n = len(nums)
first = -1
last = -1
high = n-1
low = 0

for i in range(0,n):
    mid = (low+high)//2
    if nums[mid]==target