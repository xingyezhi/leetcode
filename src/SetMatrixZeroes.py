__author__ = 'xingyezhi'
# encoding: utf-8
class Solution(object):
    def setZeroes(self, matrix):
        print matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0
        print matrix
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        print matrix

sol=Solution()
sol.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])


# [[0,0,0,5],
#  [4,3,1,4],
#  [0,1,1,4],
#  [1,2,1,3],
#  [0,0,1,1]]