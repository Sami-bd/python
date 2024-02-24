class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while True:
            if 3**i == n:
                return True
            
            elif 3**i >= n  or n <= 0:
                return False
            
            i += 1
    

