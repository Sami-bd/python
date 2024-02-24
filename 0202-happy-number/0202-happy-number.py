class Solution:
    def isHappy(self, n: int) -> bool:
        same = set()
        while n != 1 and n not in same:
            same.add(n)
            n = sum(int(i)**2 for i in str(n))
        
        if n == 1:
            return True
        else:
            return False
    
