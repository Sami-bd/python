class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            x = nums.count(i)
            if x == 1:
                return i