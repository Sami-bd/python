class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        new_s = s[::-1]

        if s == new_s:
            return True
        else:
            return False