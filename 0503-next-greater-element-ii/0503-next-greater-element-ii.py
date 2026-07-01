class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1]* (n)
        #ans = [-1]* (2*n)
        for i  in range(2 * n-1,-1,-1):
            curr = nums[i%n]
            while stack and stack[-1] <=curr:
                stack.pop()
            if (i<n):
                if not stack:
                    ans[i]=-1
                else:
                    ans[i] = stack[-1]
            stack.append(curr)
        return ans
        #return ans[:n]
        