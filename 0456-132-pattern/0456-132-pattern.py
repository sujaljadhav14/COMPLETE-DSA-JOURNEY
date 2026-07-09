class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        saved=float("-inf")
        for i in range(len(nums)-1,-1,-1):
            curr=nums[i]
            if curr<saved:
                return True
            while stack and stack[-1]<curr:
                saved=stack.pop()
            stack.append(curr)
        return False
            
        