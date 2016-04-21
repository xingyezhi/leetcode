# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def calculate(self, s):
        stack=[]
        stack2=[]
        i=0
        s=s.replace(" ","")
        while i<len(s):
            if str(s[i]).isdigit():
                number=0
                while i<len(s) and str(s[i]).isdigit():
                    number*=10
                    number+=int(s[i])
                    i+=1
                stack.append(number)
            elif s[i] in ['+','-']:
                stack2.append(s[i])
                i+=1
            elif s[i] in ['*','/']:
                j=i
                i+=1
                number=0
                while i<len(s) and str(s[i]).isdigit():
                    number*=10
                    number+=int(s[i])
                    i+=1
                if s[j]=='*':a=stack.pop()*number
                else:a=stack.pop()/number
                stack.append(a)
        a=stack[0]
        for i in range(1,len(stack)):
            a=a+stack[i] if stack2[i-1]=='+' else a-stack[i]
        return a



sol=Solution()
print sol.calculate(' 3+5 / 2 ')