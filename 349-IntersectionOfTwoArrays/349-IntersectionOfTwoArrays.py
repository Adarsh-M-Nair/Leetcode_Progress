# Last updated: 7/18/2026, 8:31:48 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        for i in nums1:
            if i in nums2:
                inter.append(i)
        return list(set(inter))