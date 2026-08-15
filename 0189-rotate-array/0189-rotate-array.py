class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Solution 
        [1,2,3,4,5,6,7]
        ↓ reverse all
        [7,6,5,4,3,2,1]
        ↓ reverse first k = 3
        [5,6,7,4,3,2,1]
        ↓ reverse remaining
        [5,6,7,1,2,3,4]
        """
        k = k%len(nums)
        # to avoid the base condition where k is > then nums of total elememts eg k=5 nums[1,2,3]
        nums.reverse()
        # reverse the 1st k elemenet
        left = 0
        right = k-1
        while (left<right):
            nums[left] , nums[right] = nums[right] ,nums[left]
            left+=1
            right-=1
        
        #reverse remaining elements 
        left = k
        right = len(nums)-1
        while(left<right):
            nums[left] , nums[right] = nums[right] , nums[left]
            left+=1
            right-=1
        return nums 
        