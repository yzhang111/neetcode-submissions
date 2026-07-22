class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs=[]
        for i, nums in enumerate(nums):
            pairs.append([nums, i])
        pairs.sort()

        left = 0
        right = len(pairs) - 1
        while (left < right):
            current_sum = pairs[left][0] + pairs[right][0]
            if (current_sum == target):
                return sorted([pairs[left][1], pairs[right][1]])
            elif (current_sum < target):
                left += 1
            else: 
                right -= 1
        return []