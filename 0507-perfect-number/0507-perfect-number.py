class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        else:
            s = 1

            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    s += i
                    complement = num // i
                    if complement != i:
                        s += complement

            if s == num:
                return True
            else:
                return False
