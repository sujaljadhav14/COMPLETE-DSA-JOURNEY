class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Less optimal
        # Squaring: O(n)
        # Sorting: O(n log n)
        # for i in range(len(nums)):
        #     nums[i] = nums[i]*nums[i]
        # nums.sort()
        # return nums

        ans = [0]*len(nums)
        left = 0
        right  , pos= len(nums)-1 , len(nums)-1

        while(left<=right):
            if(abs(nums[left])>abs(nums[right])):
                ans[pos] = nums[left]*nums[left]
                left+=1
            else:
                ans[pos] = nums[right]*nums[right]
                right-=1
            pos-=1
        return ans

            
         


        