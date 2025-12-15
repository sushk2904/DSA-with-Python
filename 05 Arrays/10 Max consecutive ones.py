nums = [0,1,1,0,0,0,1,1,1,1,1,0,0]
n = len(nums)
cons = 0
maxm_cons = 0
for i in range(0,n):
    if nums[i]==1:
        cons+=1
    else:
        maxm_cons =  max(cons, maxm_cons)
        cons = 0
print(max(maxm_cons, cons))  #Why max again? Because what if there are 6 1's in the end, they will never go to the else part since no zeros are there to break the loop. 