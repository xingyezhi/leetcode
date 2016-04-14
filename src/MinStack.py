# coding=utf-8
__author__ = 'lenovo'


class MinStack(object):
    def __init__(self):
        self.stack=[]

    def push(self, x):
        if len(self.stack)==0:
            self.stack.append((x,x))
            return
        t=self.getMin()
        self.stack.append((min(t,x),x))


    def pop(self):
        self.stack.pop()


    def top(self):
        return self.stack[-1][1]


    def getMin(self):
        return self.stack[-1][0]
minstack=MinStack()
minstack.push(3)
minstack.push(8)
minstack.push(1)
minstack.push(5)
minstack.push(2)
minstack.push(9)
minstack.push(6)
minstack.push(7)
print minstack.getMin()

