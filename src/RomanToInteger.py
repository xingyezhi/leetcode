__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        map={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        result=0
        i=0
        while i<len(s):
            if i!=len(s)-1 and map[s[i]]<map[s[i+1]]:
                result+=map[s[i+1]]-map[s[i]]
                i+=1
            else:
                result+=map[s[i]]
            i+=1
        return result

sol=Solution()
print sol.romanToInt("MCMLXXX")