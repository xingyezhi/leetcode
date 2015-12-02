__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
       if numRows==1:
          return s
       result=""
       VAL=(numRows-1)*2
       i=0
       while i<len(s):
           result+=s[i]
           i+=VAL
       for i in range(1,numRows-1):
           a=i
           b=VAL-a
           while a<len(s) and b<len(s):
               result+=s[a]+s[b]
               a+=VAL
               b+=VAL
           if a<len(s):
               result+=s[a]
           if b<len(s):
               result+=s[b]
       i=numRows-1
       while i<len(s):
           result+=s[i]
           i+=VAL
       return result

sol=Solution()
print sol.convert("A", 1)