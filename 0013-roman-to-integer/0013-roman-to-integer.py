class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.lower()

        roman_char = {
        "i": 1,
        "v": 5,
        "x": 10,
        "l": 50,
        "c": 100,
        "d": 500,
        "m": 1000
        }

        total = 0
        prev = 0

        for x in reversed(s):
            value = roman_char[x]
            if value < prev:
                total -= value
            else:
                total += value 
                prev = value

        return total
