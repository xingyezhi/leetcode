__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def minCut(self,s):
        map={}
        pair=[[False for i in range(len(s))] for j in range(len(s))]
        result=[i for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[i]==s[j] and ((i-j)<=1 or pair[j+1][i-1]):
                    pair[j][i]=True
                    if j==0:
                        result[i]=0
                    else:
                        result[i]=min(result[i],result[j-1]+1)
        return result[-1]

sol=Solution()
print sol.minCut("aab")
