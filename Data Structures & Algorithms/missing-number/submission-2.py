class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        nums_len = len(nums)
        for i in range(nums_len + 1):
            result = result ^ i
        for num in nums:
            result = result ^ num
        return result