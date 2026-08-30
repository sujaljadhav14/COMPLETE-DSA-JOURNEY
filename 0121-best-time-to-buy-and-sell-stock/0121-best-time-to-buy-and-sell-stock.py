class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = float("inf")
        max_prof = float("-inf")
        for i in prices:
            if i<mini:
                mini = i
            max_prof = max(max_prof , i-mini)
        return max_prof
        
    
    
    
    
    
    # def test:
            
            # """##optimal solution following the [today's price - cheapest so far] price approach
            # cheapest_price = float("inf")
            # profit = 0
            # for i in range(len(prices)):
            #     curr_profit = 0
            #     if cheapest_price>prices[i]:
            #         cheapest_price = prices[i]
            #     curr_profit = prices[i]-cheapest_price
            #     if(curr_profit>profit):
            #         profit=curr_profit
            # return profit

            # #brute force appproach 
            # # min_val = float("inf")
            # # max_val = float("-inf")
            # # minindex = 0
            # # for i in range(len(prices)):
            # #     if prices[i]<min_val:
            # #         min_val = prices[i]
            # #         minindex = i
            # # for i in range(minindex,len(prices)):
            # #     if prices[i]>max_val:
            # #         max_val = prices[i]
            
            # # if (max_val=="-inf"):
            # #     return 0
            # # else:
            # #     return max_val-min_val
            # """