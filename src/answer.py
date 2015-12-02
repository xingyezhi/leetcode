__author__ = 'lenovo'
# coding=utf-8

class Solution:
    def isMatch(self, s, p):
        dp=[[False for x in range(len(p)+1)] for x in range(len(s)+1)]
        dp[0][0]=True
        for j in range(0,len(p)):
            if p[j]=='*':
                dp[0][j+1]=dp[0][j-1]
        for i in range(0,len(s)):
            for j in range(0,len(p)):
                if p[j]=='*':
                    if dp[i+1][j-1]:
                        dp[i+1][j+1]=True
                    elif dp[i][j+1] and (p[j-1]=='.' or s[i]==p[j-1]):
                        dp[i+1][j+1]=True
                else:
                    if dp[i][j]==True and (s[i]==p[j] or p[j]=='.'):
                        dp[i+1][j+1]=True
        print dp
        return dp[len(s)][len(p)]













sol=Solution()
print sol.isMatch("aaa", "ab*a*c*a")

c=[[1,2,3],[4,5,6]]
print c[1][-1]