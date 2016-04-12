__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def maxProfit(self, prices):
        if prices==None or len(prices)<2:return 0
        leftmin=prices[0]
        profit=0
        for i in prices[1:]:
            profit=max(profit,i-leftmin)
            leftmin=min(leftmin,i)
        return profit