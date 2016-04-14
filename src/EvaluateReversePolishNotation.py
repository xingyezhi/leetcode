# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
  # ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  # ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
    def evalRPN(self, tokens):
        if len(tokens)==0:return 0
        stack=[]
        for i in tokens:
            try:
                stack.append(int(i))
            except ValueError:
                b=stack.pop()
                a=stack.pop()
                if i=='+':
                    stack.append(a+b)
                elif i=='-':
                    stack.append(a-b)
                elif i=='/':
                    t=1 if a*b>0 else -1
                    stack.append(t*(abs(a)/abs(b)))
                elif i=='*':
                    stack.append(a*b)
        return stack.pop()
sol=Solution()
import math
print int(2.7)
#print (-4//(11))
#print sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"] )

#22