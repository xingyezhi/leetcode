__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} s
    # @return {boolean}
    def match(self,a,b):
        if a=='[' and b==']':
            return True
        elif a=='{' and b=='}':
            return True
        elif a=='(' and b==')':
            return True
        else:
            return False
    def isValid(self, s):
        stack=[]
        for i in s:
            if i=='[' or i=='{' or i=='(':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if not self.match(top,i):
                    return False
        if len(stack)==0:
            return True
        else:
            return False

sol=Solution()
print sol.isValid("[][][][([(]))]")