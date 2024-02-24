class Solution:
    def isPalindrome(self, x: int) -> bool:
        check = x
        rem = 0
        s = 0
        if x < 0:
            return False
        while x != 0:
            rem = x%10
            s = (s*10)+rem
            x = x//10
            
        if s == check:
            return True
        else: 
            return False
    