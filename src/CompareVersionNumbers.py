# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def compareVersion(self, version1, version2):
        s1=version1.split('.')
        s2=version2.split('.')
        m=max(len(s1),len(s2))
        for i in range(m):
            if i>=len(s1):a=0
            else:a=int(s1[i])
            if i>=len(s2):b=0
            else:b=int(s2[i])
            if a>b:return 1
            elif a<b:return -1
        return 0

sol=Solution()
print sol.compareVersion("4.21","4.2")
