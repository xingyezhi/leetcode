__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def titleToNumber(self, s):
        result=0
        for i in s:
            result*=26
            result+=ord(i)-64
        return result

t='A'
print ord(t)
sol=Solution()
print sol.titleToNumber('AB')