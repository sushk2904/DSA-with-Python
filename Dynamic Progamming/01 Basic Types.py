"""FOR FIBONNACI"""


#Recursion















#Memoization
class Solution:
    def fib(self, n):
        dp = [-1]*(n+1)
        def solve(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if dp[num] != -1:
                return dp[num]
            dp[num] = solve(num-1) + solve(num-2)
            return dp[num]
        return solve(n)



#Tabulation
class Tabulation:
    def fibb(self,n):
        dp = [-1]*(n+1)
        def solvee(num):
            dp[0] = 0
            dp[1] = 1
            for num in range(2, n+1):
                dp[num] = dp[num-1] + dp[num-2]

            return dp[num]
        return solvee(n)

#Tabulation with space optimization 
class OptimizedTabulation:
    def fibbb(self, n):
        def solve(num):
            prev = 1
            prev1 = 0
            curr = 0
            for i in range(2,n+1):
                curr = prev + prev1
                prev1 = prev 
                prev = curr
            return prev
        return solve(n)
                












