__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def generate(self, numRows):
        if numRows==0:return []
        result=[[1]]
        for i in range(1,numRows):
            temp=[1]
            for j in range(1,i):
                temp.append(result[i-1][j]+result[i-1][j-1])
            temp.append(1)
            result.append(temp)
        return result

sol=Solution()
sol.generate(6)
