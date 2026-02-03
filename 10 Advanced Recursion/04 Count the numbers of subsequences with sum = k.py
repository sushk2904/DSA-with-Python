def backtrack(index, total):
    if total == k:
        return 1
    if total > k:
        return 0
    if index >= len(nums):
        return 0
    sum = total + nums[index]
    pick = backtrack(index+1, total)
    sum = total
    n_pick = backtrack(index+1, total)
    count = pick + n_pick
    print(count)
    