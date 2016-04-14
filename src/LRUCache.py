# coding=utf-8
__author__ = 'lenovo'
from collections import deque
class LRUCache(object):

    def __init__(self, capacity):
        self.cache={}
        self.capacity=capacity
        self.queue=deque([])

    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            self.cache[key]=value
            self.queue.remove(key)
            self.queue.append(key)
            return
        if len(self.cache)<self.capacity:
            self.cache[key]=value
            self.queue.append(key)
        else:
            k=self.queue.popleft()
            del self.cache[k]
            self.cache[key]=value
            self.queue.append(key)

sol=LRUCache(2)
sol.set(2,1)
sol.set(1,1)
sol.set(2,3)
sol.set(4,1)
print sol.get(1)
print sol.get(2)


# 2,[set(2,1),set(1,1),set(2,3),set(4,1),get(1),get(2)]
