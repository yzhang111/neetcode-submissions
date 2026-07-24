class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            previous = s

            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

            if previous == s:
                break
        return s == ""