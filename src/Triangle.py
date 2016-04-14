__author__ = 'xingyezhi'
# encoding: utf-8


class Solution(object):
    def minimumTotal(self, triangle):
        result=[0]*len(triangle)
        for i in range(len(triangle)):
            for j in range(i,-1,-1):
                if j==i:
                    result[j]=triangle[i][j]+result[j-1]
                elif j==0:
                    result[j]=triangle[i][j]+result[j]
                else:
                    result[j]=triangle[i][j]+min(result[j],result[j-1])
        return min(result)
sol=Solution()
print sol.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])