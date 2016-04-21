# coding=utf-8
__author__ = 'lenovo'

import re
class Solution(object):
    def cal(self,s):
        #print s
        s=s.replace(" ","")
        pattern=re.compile('[+-]')
        number=[int(i) if i[0]!='*' else -int(i[1:]) for i in pattern.split(s)]
        symble=pattern.findall(s)
        if len(number)==0:return 0
        a=number[0]
        for i in range(len(symble)):
            a=a+number[i+1] if symble[i]=='+' else a-number[i+1]
        return a

    def calculate(self, s):
        stack=[]
        s='('+s+")"
        for i in s:
            if i!=')':
                stack.append(i)
            else:
                temp=[]
                while stack[-1]!='(':
                    temp.append(stack.pop())
                stack.pop()
                result=self.cal(''.join(temp[::-1]))
                if result<0:
                    stack.append('*'+str(-result))
                else:
                    stack.append(str(result))
        result=stack[-1]
        return int(result) if result[0]!='*' else -int(result[1:])
sol=Solution()
print sol.calculate("2-(5-6)")
