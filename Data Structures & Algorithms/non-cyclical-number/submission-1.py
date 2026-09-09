class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n 
        slow = n
        while True:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False

    def get_next(self, n: int) -> int:
        result = 0

        while n > 0: 
            digit = n % 10
            result += digit * digit
            n = n // 10
        return result

