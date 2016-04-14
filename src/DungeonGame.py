__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m,n=len(dungeon),len(dungeon[0])
        map=[[0 for i in range(n)] for j in range(m)]
        map[m-1][n-1]=min(dungeon[m-1][n-1],0)
        for i in range(m-2,-1,-1):
            map[i][n-1]=min(map[i+1][n-1]+dungeon[i][n-1],0)
        for i in range(n-2,-1,-1):
            map[m-1][i]=min(map[m-1][i+1]+dungeon[m-1][i],0)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                map[i][j]=min(max(map[i+1][j],map[i][j+1])+dungeon[i][j],0)
        if map[0][0]>0:
            return 1
        else:
            return -map[0][0]+1


sol=Solution()
print sol.calculateMinimumHP([[0,5],[-2,-3]])