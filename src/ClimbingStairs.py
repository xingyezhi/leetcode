__author__ = 'xingyezhi'
# encoding: utf-8
class Solution(object):
    def climbStairs(self, n):
        if n in [1,2]:return n
        a,b=1,2
        for i in range(n-2):
            b,a=a+b,b
        return b

sol=Solution()
print sol.climbStairs(5)