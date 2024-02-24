class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:        
        i = 0
        for index, element in enumerate(nums):
            if element == target:
                return index
                
            elif target > element:
                i = i + 1
                
        return i
    