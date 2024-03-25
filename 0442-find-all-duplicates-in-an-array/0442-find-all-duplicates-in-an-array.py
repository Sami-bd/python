class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = [i for i in nums if 1<nums.count(i)]

        dup = list(set(dup))

        return dup