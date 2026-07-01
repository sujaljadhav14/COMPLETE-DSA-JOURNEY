class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        stack =[]
        ans =[]
        for i in range(len(nums2)-1,-1,-1):
            curr = nums2[i]
            while stack and stack[-1]<=curr:
                stack.pop()
            if not stack:
                freq[curr] = -1
            else:
                freq[curr] = stack[-1]
            stack.append(curr)
            
        for i in nums1:
                ans.append(freq[i])
        return ans
        