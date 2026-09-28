class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for count, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num]+1,count+1]
            dic[num] = count
        return []