class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            dup = nums.count(i)
            
            if dup > 1:
                return i
            