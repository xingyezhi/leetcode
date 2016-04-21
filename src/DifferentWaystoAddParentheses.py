# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def diffWaysToCompute(self, input):
        import re
        pattern=re.compile('[*+-]')
        numlist=[int(i) for i in pattern.split(input)]
        symlist=pattern.findall(input)
        dp=[[[] for i in range(len(numlist))] for j in range(len(numlist))]
        for i in range(len(numlist)):
            dp[i][i].append(numlist[i])
        for i in range(1,len(numlist)):
            for j in range(len(numlist)-i):
                for k in range(j,j+i):
                    result1=dp[j][k]
                    result2=dp[k+1][i+j]
                    for l1 in result1:
                        for l2 in result2:
                            if symlist[k]=='+':
                                dp[j][j+i].append(l1+l2)
                            elif symlist[k]=='*':
                                dp[j][j+i].append((l1*l2))
                            else:
                                dp[j][j+i].append(l1-l2)
        return dp[0][len(numlist)-1]
sol=Solution()
print sol.diffWaysToCompute("2-4+5")
