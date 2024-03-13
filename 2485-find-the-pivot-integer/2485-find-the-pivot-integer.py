class Solution:
    def pivotInteger(self, n: int) -> int:
        add = 0

        while n:
            sum_n = int(n*(n+1)/2)
            add += n
            
            if sum_n == add:
                return n
            n -= 1
            
        return -1