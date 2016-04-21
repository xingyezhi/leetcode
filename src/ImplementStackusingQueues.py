# coding=utf-8
__author__ = 'lenovo'
from collections import deque

class Stack(object):
    def __init__(self):
        self.q1=deque()
        self.q2=deque()


    def push(self, x):
        self.q2.appendleft(x)
        while len(self.q1)!=0:
            self.q2.appendleft(self.q1.pop())
        self.q1,self.q2=self.q2,self.q1


    def pop(self):
        return self.q1.pop()


    def top(self):
        return self.q1[len(self.q1)-1]


    def empty(self):
        return len(self.q1)==0
