class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        for num,count in freq.items():
            bucket[count].append(num)
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
#cooked me ~~ make sure to pratice again whenever come here         


            
            
            
            
            
            
