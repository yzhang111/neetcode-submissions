class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climb(n, memo)


    def climb(self, n: int,memo: dict) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in memo:
            return memo[n]
        
        result = self.climb(n-1, memo) + self.climb(n-2, memo)
        memo[n] = result
        return result