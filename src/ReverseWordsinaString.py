# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
#"the sky is blue"
#"blue is sky the"
    def reverseWords(self, s):
        result=[]
        s=s.strip()
        strlist=s.split(" ")
        result=[i for i in strlist if i!=""]
        return " ".join(result[::-1])

sol=Solution()
sol.reverseWords("")
