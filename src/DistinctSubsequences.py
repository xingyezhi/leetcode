__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def numDistinct(self, s, t):
        fs=[i for i in s if i in t]
        temp=[1 for i in range(len(fs)+1)]
        dp=[0 for i in range(len(fs)+1)]
        for i in t:
            for j in range(len(fs)):
                if i==fs[j]:
                    dp[j+1]=dp[j]+temp[j]
                else:
                    dp[j+1]=dp[j]
            temp=dp[:]
        print dp[len(fs)]


sol=Solution()
sol.numDistinct("rrabbaeeeebit","rabbit")