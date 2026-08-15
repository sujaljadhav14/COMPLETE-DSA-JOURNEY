class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = sum(nums)
        exp_sum = (n *( n+1)/2)
        return int(exp_sum - actual_sum)
        