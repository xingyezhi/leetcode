# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def isIsomorphic(self, s, t):
        map={}
        for i in range(len(s)):
            if s[i] in map and map[s[i]]!=t[i]:return False
            else:map[s[i]]=t[i]
        map={}
        s,t=t,s
        for i in range(len(s)):
            if s[i] in map and map[s[i]]!=t[i]:return False
            else:map[s[i]]=t[i]
        return True

sol=Solution()
print sol.isIsomorphic("ab", "aa")