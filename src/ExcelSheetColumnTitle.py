__author__ = 'xingyezhi'
# encoding: utf-8


class Solution(object):
    def convertToTitle(self, n):
        result=[]
        alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while n!=0:
            result.append(alpa[(n-1)%26])
            n=(n-1)/26
        return ''.join(result[::-1])

sol=Solution()
print sol.convertToTitle(27)