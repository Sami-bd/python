class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        loop = True
        x, y = 0, 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i]+nums[j]
                if s == target:
                    return [i, j]
                    loop = False
                    break

            if loop == False:
                break

            

        
