class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        i,j = 0, 0
        result = []
        while j < len(s):
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1: j+1+length])
            i,j = j+1+length,j+1+length
        return result
