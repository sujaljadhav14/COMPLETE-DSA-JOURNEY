class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        count = 0
        hashmap={0:1}
        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix%k
            if rem in hashmap:
                count+=hashmap[rem]
            hashmap[rem] = hashmap.get(rem, 0) + 1
        return count
## more ezzzy
