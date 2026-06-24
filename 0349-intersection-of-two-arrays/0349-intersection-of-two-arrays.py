class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        ans=set()
        for i in nums2:
            if i in set1:
                ans.add(i)
        ans=list(ans)
        return ans

        