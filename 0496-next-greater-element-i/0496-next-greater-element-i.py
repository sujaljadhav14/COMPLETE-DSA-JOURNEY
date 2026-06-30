class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextgreat_elem = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            current = nums2[i]
            ans = 0
            while stack and stack[-1]<=current:
                stack.pop()
            if stack==[]:
                ans = -1
            else:
                ans = stack[-1]
            nextgreat_elem[current] = ans
            stack.append(current)
        answer = []
        for num in nums1:
            answer.append(nextgreat_elem[num])
        return answer




            
        

        