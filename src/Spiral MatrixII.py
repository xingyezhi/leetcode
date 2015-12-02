__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            B=zip(*A[::-1])
            A = [range(lo, hi)] + B
        return A

sol=Solution()
print sol.generateMatrix(3)

a=[range(0,1)]
b=[[6,7],(9,8)]
print len(b)
