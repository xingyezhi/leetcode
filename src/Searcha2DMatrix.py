__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def searchMatrix(self, matrix, target):
        m,n=len(matrix),len(matrix[0])
        left,right=0,m*n
        while left<right:
            middle=left+(right-left)/2
           # if middle>=m*n:return False
            if matrix[middle/n][middle%n]==target:return True
            elif matrix[middle/n][middle%n]<target:left=middle+1
            else:right=middle
        if left>=m*n:return False
        return matrix[left/n][left%n]==target




sol=Solution()
print sol.searchMatrix([[1,1]],0)
