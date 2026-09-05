class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if count != nums[i]:
                return count
            count += 1
        return count