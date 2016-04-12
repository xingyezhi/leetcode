# coding=utf-8
__author__ = 'lenovo'
class Solution(object):
    def maxProfit(self, k,prices):
        profit=0
        if k>len(prices)/2:
            return self.quicksove(prices)
        dp=[[0 for i in range(len(prices))] for j in range(3)]
        for i in range(1,k+1):
            copyprofit=profit
            profit=0
            for j in range(1,len(prices)):
                dp[1][j],dp[0][j]=dp[2][j],dp[1][j]
                if prices[j]>prices[j-1]:
                    dp[1][j]=max(dp[0][j],dp[1][j-1]+prices[j]-prices[j-1])
                else:
                    dp[2][j]=profit
                    dp[1][j]=max(dp[1][j],dp[1][j-1]+prices[j]-prices[j-1])
                profit=max(profit,dp[1][j])
            if profit==copyprofit:return profit
        return profit
    def quicksove(self,prices):
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit
sol=Solution()
print sol.maxProfit(4,[1,2,4,2,5,7,2,4,9,0])