class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while(left < right):
            charLeft = s[left]
            charRight = s[right]
            if not charLeft.isdigit() and not charLeft.isalpha():
                left += 1
                continue

            if not charRight.isdigit() and not charRight.isalpha():
                right -= 1
                continue

            if charLeft.casefold() != charRight.casefold(): 
                return False
            
            left +=1
            right -= 1

        return True