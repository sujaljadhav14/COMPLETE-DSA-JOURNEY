class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        left = 0
        right = n
        while (left<n):
            ans.append(nums[left])
            left+=1
            ans.append(nums[right])
            right+=1
        return ans

        