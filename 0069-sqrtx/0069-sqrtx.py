class Solution:
    def mySqrt(self, x: int) -> int:
        # n = 8
        temp = x
        root = []
        n = 1
        if x == 0:
            return 0

        while n*n <= temp:
            root.append(n)
            n += 1

        return root[-1]




