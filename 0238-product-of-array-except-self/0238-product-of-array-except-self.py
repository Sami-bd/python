class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my_code this is comment line
        # answer = []
        # for i in range(len(nums)):
        #     prod = 1

        #     for j in range(len(nums)):
        #         if i != j:
        #             prod *= nums[j]
        #     answer.append(prod)
                
        # return answer

        n = len(nums)
        
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        answer = [prefix[i] * suffix[i] for i in range(n)]
        
        return answer