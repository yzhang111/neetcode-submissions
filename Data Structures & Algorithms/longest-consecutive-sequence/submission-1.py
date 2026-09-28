class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longestL = 0
        for num in numset:
            if num - 1 not in numset:
                currentN = num
                currentL = 1
                while currentN+1 in numset:
                    currentN += 1
                    currentL += 1
                longestL = max(longestL, currentL)
        return longestL