class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n not in seen:
                seen.add(n)
                n = self.get_next(n)
            else:
                return False
        return True

    def get_next(self, n: int) -> int:
        result = 0

        while n > 0: 
            digit = n % 10
            result += digit * digit
            n = n // 10
        return result

