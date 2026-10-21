class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
            Complexity:
            - Time: O(n) — both pointers move inward, processing the array in one pass.
            - Space: O(1) — in-place swapping; no extra result array.
        """
        left = 0
        right = len(nums)-1
        while(left<right):
            if(nums[left]%2==0):
                left+=1
            elif(nums[right]%2!=0):
                right-=1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1   
        return nums

        """Complexity:
            - Time: O(n) — two passes through the array.
            - Space: O(n) — the new result array.
        """
        # ans = []
        # for i in nums:
        #     if(i%2==0):
        #         ans.append(i)
        # for i in nums:
        #     if(i%2!=0):
        #         ans.append(i)
        # return ans
        