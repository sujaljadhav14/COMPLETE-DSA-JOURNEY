class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        #brute force
        newnum = set(nums)
        ans = []
        for i in range(1,   len(nums)+1):
            if i not in newnum:
                ans.append(i)
        return ans

    #     #optimal sol
    #   # Mark numbers that we have seen
    #     for i in range(len(nums)):
    #         index = abs(nums[i]) - 1
    #         nums[index] = -abs(nums[index])

    #     ans = []

    #     # Positive index means that number was never seen
    #     for i in range(len(nums)):
    #         if nums[i] > 0:
    #             ans.append(i + 1)

    #     return ans
