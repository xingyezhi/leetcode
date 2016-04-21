# coding=utf-8
__author__ = 'lenovo'

class Queue(object):
    def __init__(self):
        self.stack=[]


    def push(self, x):
        temp=[]
        while len(self.stack)!=0:
            temp.append(self.stack.pop())
        self.stack.append(x)
        while len(temp)!=0:
            self.stack.append(temp.pop())


    def pop(self):
        return self.stack.pop()


    def peek(self):
        return self.stack[-1]


    def empty(self):
        return len(self.stack)==0
