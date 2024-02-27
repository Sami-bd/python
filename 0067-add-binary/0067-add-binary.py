class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_1, decimal_2 = int(a, 2), int(b, 2)

        summ = decimal_1+decimal_2

        summ = str(bin(summ)[2:])

        return summ