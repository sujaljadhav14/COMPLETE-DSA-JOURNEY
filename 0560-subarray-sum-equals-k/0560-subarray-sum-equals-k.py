class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        hashmap = {0:1}
        count = 0
        for i in nums:
            prefix+=i
            need = prefix - k
            if need in hashmap:
                count += hashmap[need]
            hashmap[prefix] = hashmap.get(prefix , 0)+1
        return count
       