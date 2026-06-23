class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        longest=0
        for i in set_num:
            if i-1 not in set_num:
                current = i
                length=1
                while(current+1 in set_num):
                    current+=1
                    length+=1
                longest=max(longest,length)
        return longest 
