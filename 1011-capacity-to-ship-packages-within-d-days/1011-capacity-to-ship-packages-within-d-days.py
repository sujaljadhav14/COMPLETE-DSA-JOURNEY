class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canship(capacity):
            day_nd=1
            curr_weig=0
            for i in weights:
                if curr_weig+i<=capacity:
                    curr_weig+=i
                else:
                    curr_weig=i
                    day_nd+=1
            if(day_nd<=days):
                return True
            else:
                return False
        
        left=max(weights)
        right=sum(weights)
        while(left<right):
            mid=(left+right)//2
            if canship(mid):
                right=mid
            else:
                left=mid+1
        return left
        