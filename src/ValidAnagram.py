# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def isAnagram(self, s, t):
        a,b=list(s),list(t)
        a.sort()
        b.sort()
        return a==b
sol=Solution()
print sol.isAnagram("cat","tac")