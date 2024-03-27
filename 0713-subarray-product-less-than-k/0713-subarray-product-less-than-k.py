class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # subarrays = []
        # n = len(nums)
        # count = 0

        # # Generate all possible subarrays
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         mul = 1
        #         subarray = nums[i:j]
        #         for m in subarray:
        #             mul = mul * m
                
        #         if mul < k:
        #             count += 1
            
        # return count

        if k <= 1:
            return 0

        left, right, product, count = 0, 0, 1, 0
        n = len(nums)

        while right < n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1

        return count