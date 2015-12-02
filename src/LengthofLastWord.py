__author__ = 'lenovo'
# coding=utf-8


class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        slist=s.split(' ')
        return len(slist[-1]) if len(slist)!=0 else 0

sol=Solution()
print sol.lengthOfLastWord(" ab  cd")