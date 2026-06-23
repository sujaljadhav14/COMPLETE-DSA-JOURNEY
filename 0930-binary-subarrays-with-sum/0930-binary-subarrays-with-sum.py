class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        count = 0
        hashmap={0:1}
        for i in nums:
            prefix+=i
            need = prefix -goal
            if need in hashmap:
                count+=hashmap[need]
            hashmap[prefix]=hashmap.get(prefix,0)+1
        return count
# same as 560 can be optimize with sliding window~~