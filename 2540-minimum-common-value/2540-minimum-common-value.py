class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1).intersection(nums2)

        if common:
            return (min(list(common)))
            
        else:
            return -1