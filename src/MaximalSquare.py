__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix)==0:return 0
        m,n=len(matrix),len(matrix[0])
        col,dp=[0]*n,[[0 for i in range(n)] for j in range(m)]
        result=0
        for i in range(m):
            row=[0]*n
            for j in range(n):
                row[j]=int(matrix[i][j]) and int(matrix[i][j])+row[j-1]
                col[j]=int(matrix[i][j]) and int(matrix[i][j])+col[j]
                if i==0 or j==0:
                    dp[i][j]=int(matrix[i][j])
                else:
                    if row[j]>dp[i-1][j-1] and col[j]>dp[i-1][j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=min(row[j],col[j])
                result=max(result,dp[i][j])
        #print dp
        return result*result

# sol=Solution()
# print sol.maximalSquare(["1010","1011","1011","1111"])



