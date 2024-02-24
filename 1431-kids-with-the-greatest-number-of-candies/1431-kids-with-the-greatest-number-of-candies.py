class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest_number = max(candies)


        candies = [True if i+extraCandies >= largest_number else False for i in candies]

        return candies