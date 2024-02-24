class Solution:
    def reverse(self, x: int) -> int:
        # x = 1534236469
        x_abs = abs(x)

        check = (1 if x >= 0 else -1)
        div = 0
        reverse = 0
        while x_abs:
            div = x_abs % 10
            reverse = (reverse * 10) + div
            x_abs //= 10
            
        reverse = reverse*check

        if -2**31 <= reverse <= 2**31-1:
            return reverse
            
        else:
            return 0

    




