class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def canmakeBouquets(day):
            bouq = 0
            adaj =0
            for flower in bloomDay:
                if flower <= day:
                    adaj+=1
                    if adaj==k:
                        bouq+=1
                        adaj=0
                else:
                    adaj=0
            if bouq>=m:
                return True
            else:
                return False
        
        left=min(bloomDay)
        right=max(bloomDay)
        while(left<right):
            mid=(left+right)//2
            if(canmakeBouquets(mid)):
                right=mid
            else:
                left=mid+1
        return left