__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def maxProfit(self, prices):
        k,profit=2,0
        dp=[[0 for i in range(len(prices))] for j in range(k+2)]
        for i in range(1,k+1):
            for j in range(1,len(prices)):
                if prices[j]>prices[j-1]:
                    dp[i][j]=dp[i][j-1]+prices[j]-prices[j-1]
                else:
                    dp[i+1][j]=profit
                    dp[i][j]=max(dp[i][j],dp[i][j-1]+prices[j]-prices[j-1])

                profit=max(profit,dp[i][j])
        print dp
        return profit

sol=Solution()
print sol.maxProfit([3,2,6,5,0,3])