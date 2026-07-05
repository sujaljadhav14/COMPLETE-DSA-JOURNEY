class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def check_ther(value):
            thrs=0
            for i in nums:
                curr_div=(i+value-1)//value
                thrs+=curr_div
            if(thrs<=threshold):
                return True
            else:
                return False
        
        left=1
        right=max(nums)
        while(left<right):
            mid=(left+right)//2
            if check_ther(mid):
                right=mid
            else:
                left=mid+1
        return left   