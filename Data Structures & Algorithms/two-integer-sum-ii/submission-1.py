class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftP = 0
        rightP = len(numbers) - 1
        while leftP != rightP:
            sum = numbers[leftP] + numbers[rightP]
            if sum == target:
                return[leftP + 1, rightP + 1]
            elif sum < target:
                leftP += 1
            else:
                rightP -= 1
        return [] 