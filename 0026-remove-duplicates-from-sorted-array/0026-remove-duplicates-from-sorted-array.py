class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        for i in range(len(nums)):
            if(nums[left]==nums[i]):
                pass
            else:
                left+=1
                nums[left] = nums[i]
        return left+1

            

        

        