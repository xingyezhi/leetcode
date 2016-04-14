# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def numIslands(self, grid):
        if len(grid)==0:return 0
        self.m,self.n=len(grid),len(grid[0])
        result=0
        self.visit=[[False for i in range(self.n)]for j in range(self.m)]
        self.position=[[-1,0],[1,0],[0,1],[0,-1]]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]=='0' or self.visit[i][j]:
                    continue
                else:
                    self.dfs(i,j,grid)
                    result+=1
        return result
    def dfs(self,i,j,grid):
        self.visit[i][j]=True
        for pos in self.position:
            x,y=i+pos[0],j+pos[1]
            if 0<=x<self.m and 0<=y<self.n and not self.visit[x][y] and grid[x][y]=='1':
                self.dfs(x,y)