class Solution:
    def maxProfit(self,prices: List[int]) -> int:
        List= [1,2,3,4,5]
        l,r = 0,1  
        maxP = 0
        
        while r < len(prices):
            #iterate through prices
            if prices[l] < prices[r]:
                #buy at low and sell at high
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
                #update the maxProfit
            else:
                l = r  #we wanted left pointer to be low
            r += 1 #gone through all values
        return maxP
