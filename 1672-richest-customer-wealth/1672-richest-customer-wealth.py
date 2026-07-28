class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_val = []
        for i in accounts:
            max_val.append(sum(i))
        return max(max_val)





        
        