class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # return ((nums[-1]-1)*(nums[-2]-1))
        larg=0
        sec_larg=0
        for i in nums:
            if larg<=i:
                sec_larg = larg
                larg=i
            elif i>sec_larg:
                sec_larg = i
        return ((larg-1)*(sec_larg-1))
#optimize
# Use a for loop to find two variable large and second large and then done the operation
        