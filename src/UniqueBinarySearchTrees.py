# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def numTrees(self, n):
        a=b=1
        for i in range(n+1,2*n+1):
            a=a*i
        for i in range(1,n+2):
            b=b*i
        return a/b

sol=Solution()
print sol.numTrees(3)