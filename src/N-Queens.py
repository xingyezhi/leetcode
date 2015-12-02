__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def dfs(self,i,cur,middle):
        if i==self.n:
            map=[['.' for a in range(self.n)]for b in range(self.n)]
            for i in range(len(cur)):
                map[i][cur[i]]='Q'
            temp=[''.join(map[i]) for i in range(self.n)]
            self.result.append(temp)
            return
        else:
            for j in range(self.n):
               # print i,j
                if (not middle[0][j]) and (not middle[1][j+i]) and (not middle[2][j-i+self.n]):
                    cur[i]=j
                    middle[0][j]=middle[1][j+i]=middle[2][j-i+self.n]=1
                    self.dfs(i+1,cur,middle)
                    middle[0][j]=middle[1][j+i]=middle[2][j-i+self.n]=0

    def solveNQueens(self, n):
        self.n=n
        self.result=[]
        self.dfs(0,[0 for i in range(n)],[[0 for i in range(2*n)]for j in range(3)])
        return self.result
sol=Solution()
print sol.solveNQueens(4)
