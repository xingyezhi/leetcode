__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if len(haystack)==0 and len(needle)!=0:
            return -1
        elif len(haystack)==0 and len(needle)==0:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(i,i+len(needle)):
                if haystack[j]!=needle[j-i]:
                    break
            else:
                return i
        else:
            return -1

sol=Solution()
print sol.strStr("","")