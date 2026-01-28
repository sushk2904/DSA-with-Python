def backtrack(index, total, subset):
    if total == k: #k = target
        result.append(subset.copy())
        return
    elif total>k:
        return
    if index >=len(nums):
        return
    subset.append(nums[index])
    sum = total + nums[index]
    backtrack(index+1, sum, subset)
    e = subset.pop()
    sum = sum -e
    backtrack(index+1, total, subset)
