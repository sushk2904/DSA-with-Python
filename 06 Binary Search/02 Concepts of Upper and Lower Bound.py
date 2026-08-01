#Concepts of Upper and Lower Bound
target = 2
nums =[1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(nums)
lb = -1
low, high = 0, n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]>=target:
        lb = mid
        high = mid-1
    else:
        low = mid+1

print(lb)