__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def dfs(self,i,middle):
        if i==self.n:
            self.result+=1
            return
        else:
            for j in range(self.n):
               # print i,j
                if (not middle[0][j]) and (not middle[1][j+i]) and (not middle[2][j-i+self.n]):
                    middle[0][j]=middle[1][j+i]=middle[2][j-i+self.n]=1
                    self.dfs(i+1,middle)
                    middle[0][j]=middle[1][j+i]=middle[2][j-i+self.n]=0

    def totalNQueens(self, n):
        self.n=n
        self.result=0
        self.dfs(0,[[0 for i in range(2*n)]for j in range(3)])
        return self.result
sol=Solution()
print sol.solveNQueens(4)
#Line 30: AttributeError: 'Solution' object has no attribute 'totalNQueens'