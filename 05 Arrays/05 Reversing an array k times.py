def reverse(nums,left,right):
    
    n=len(nums)
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        right -=1
        left  +=1
    print(nums)
reverse([3, 1, 4, 2, 0, 9, 5, 8],0,7)

#1st use of reverse([2,4,1,3,8,5,9,0],4,7)
#[2, 4, 1, 3, 0, 9, 5, 8]

#2nd use of reverse([2, 4, 1, 3, 0, 9, 5, 8],0,3)
#[3, 1, 4, 2, 0, 9, 5, 8]

#3rd use of reverse([3, 1, 4, 2, 0, 9, 5, 8],0,7)
#[8, 5, 9, 2, 4, 1, 3, 0]




