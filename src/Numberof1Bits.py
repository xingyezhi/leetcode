# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def hammingWeight(self, n):
        result=0
        for i in range(32):
            if (n>>i)&1:
                result+=1
        return result
