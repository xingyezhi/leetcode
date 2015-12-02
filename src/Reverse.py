__author__ = 'lenovo'
# coding=utf-8
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        t=str(x)
        t=t[::-1]
        if x<0:
            return -int(t[:-1])
        else:
            return int(t)

sol=Solution()
print sol.reverse(-3341)