__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def rotate(self, matrix):
        size=len(matrix)-1
        for i in range((size)/2+1):
            l=size-i*2
            for j in range(i,i+l):
                starti,startj=j,size-i
                temp=matrix[i][j]
                while starti!=i or startj!=j:
                    matrix[starti][startj],temp=temp,matrix[starti][startj]
                    starti,startj=startj,size-starti
                matrix[i][j]=temp



sol=Solution()
sol.rotate([
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]
])
