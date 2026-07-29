def BinarySearch(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    while high>=low:
        mid = (low+high)//2
        if nums[mid]== target:
            return mid
        elif nums[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return mid
print(BinarySearch([1,2,3,4,5,6,7,8,9,10], 2))