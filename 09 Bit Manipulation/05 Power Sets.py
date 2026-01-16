nums = [1,2,3]
n = len(nums)
total_subsets = 1<<n
result = []
for i in range(0, total_subsets):
    lst = []
    for i in range(0,n):
        if (nums & (1<<i))!=0:
            lst.append[nums[i]]
    result.append[lst]
print("the subsets are:", result)


