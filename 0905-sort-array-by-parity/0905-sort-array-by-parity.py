class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        """Complexity:
            - Time: O(n) — two passes through the array.
            - Space: O(n) — the new result array.
        """
        ans = []
        for i in nums:
            if(i%2==0):
                ans.append(i)
        for i in nums:
            if(i%2!=0):
                ans.append(i)
        return ans
        