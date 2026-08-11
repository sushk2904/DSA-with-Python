#Iterative Solution for Binary Search
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
    return -1
print(BinarySearch([1,2,3,4,5,6,7,8,9,10], 2))


#Recursive Solution
def RecursiveBinarySearch(nums, target, low, high):
    if low > high:
        return -1
    mid =  (low + high)//2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return RecursiveBinarySearch(nums, target, low+1, high)
    else:
        return RecursiveBinarySearch(nums, target, low, high-1)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(RecursiveBinarySearch(nums, 2, 0, len(nums)-1))