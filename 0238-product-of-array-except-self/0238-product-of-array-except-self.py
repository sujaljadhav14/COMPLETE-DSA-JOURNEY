class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create the left and right product
        left = [1]* len(nums)   
        right = [1]* len(nums)
        for i in range(1 , len(nums)):
            left[i]=left[i-1]*nums[i-1]
        for i in range(len(nums)-2 , -1 , -1):
            right[i]=right[i+1]*nums[i+1]
        # add every product in this ans list
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i]=left[i]*right[i]
        return ans
