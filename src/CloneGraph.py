__author__ = 'xingyezhi'
# encoding: utf-8



# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        if node==None:return None
        map={}
        queue=[node]
        map[node.label]=UndirectedGraphNode(node.label)
        while len(queue)>0:
            top=queue.pop()
            for i in top.neighbors:
                if not map.has_key(i.label):
                    queue.append(i)
                    map[i.label]=UndirectedGraphNode(i.label)
                map[top.label].neighbors.append(map[i.label])
        return map[node.label]


t=[1,[1,2,[1,1],3]]
import copy
t2=copy.deepcopy(t)
t[1][2].append(4)
print t,t2