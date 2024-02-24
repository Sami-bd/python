class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_value = int("".join(str(num) for num in digits)) + 1

        digit_char = str(digit_value)

        digits = [int(char) for char in digit_char]

        return digits
        # print(digits)