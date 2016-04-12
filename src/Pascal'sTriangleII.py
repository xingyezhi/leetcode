__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def getRow(self, rowIndex):
        rowIndex+=1
        temp=[0 for i in range(rowIndex)]
        for i in range(rowIndex):
            for j in range(i,-1,-1):
                if j==0 or j==i:
                    temp[j]=1
                else:
                    temp[j]=temp[j]+temp[j-1]
        return temp

sol=Solution()
print sol.getRow(5)