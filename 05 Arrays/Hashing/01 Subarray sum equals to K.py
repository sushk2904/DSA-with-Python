class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        count = 0
        prefix_sum_map = {0:1}

        for num in nums:
            curr_sum += num

            if (curr_sum - k) in prefix_sum_map:
                count+= prefix_sum_map[curr_sum-k]

            if curr_sum in prefix_sum_map:
                prefix_sum_map[curr_sum] +=1
            else:
                prefix_sum_map[curr_sum] = 1
        return count