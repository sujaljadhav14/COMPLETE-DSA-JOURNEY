class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans=[-1]* len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            curr = temperatures[i]
            while stack and temperatures[stack[-1]] <=curr:
                stack.pop()
            if not stack:
                ans[i] =0
            else:
                ans[i]= stack[-1] - i
            stack.append(i)
        return ans