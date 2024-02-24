class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        l = len(s.split())
        s = s.split()
        return len(s[l-1])