n = len(nums)
if len == 1:
    return 1
freq={}
for i in range(0,n):
    if nums[i] in freq:
        freq[nums[i]] +=1
    else:
        freq[nums[i]]= 1
for k,u in freq.items():
        if u==1:
return k

#I might quit soon from this seeing the growth of the Ai :- this is the only commit for today
