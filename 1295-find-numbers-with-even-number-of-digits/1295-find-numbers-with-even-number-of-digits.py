class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            digit_count=0
            while(n!=0):
                n = n//10
                digit_count+=1
            if digit_count%2==0:
                count+=1
        return count
        