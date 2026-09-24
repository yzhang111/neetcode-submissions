class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        leftP = 1
        for num in nums:
            results.append(leftP)
            leftP *= num
        
        rightP = 1
        for j in range(len(nums)-1, -1, -1):
            results[j] *= rightP
            rightP *= nums[j]
               
        return results