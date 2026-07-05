class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(speed):
            hours=0
            for i in piles:
                curr_hr=(i+speed-1)//speed
                hours+=curr_hr
            if hours<=h:
                return True
            else:
                return False
        left=1
        right=max(piles)
        while(left<right):
            mid=(left+right)//2
            if canfinish(mid):
                right=mid
            else:
                left=mid+1
        return left