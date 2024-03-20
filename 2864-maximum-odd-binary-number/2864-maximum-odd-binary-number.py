# ========== Solution ===========

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = s.count('1')
        count_0 = s.count('0')
        ans = '1' * (count_1 - 1) + '0' * count_0 + '1'
        return ans