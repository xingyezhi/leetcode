# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        self.map=[[]for i in range(numCourses)]
        self.result=[]
        for course in prerequisites:
            self.map[course[1]].append(course[0])
        self.visit=[False for i in range(numCourses)]
        self.pos={}
        for i in range(numCourses):
            if i not in self.pos and self.dfs(i):
                return []
        return self.result[::-1]
    def dfs(self,cur):
        if cur in self.pos:return False
        elif self.visit[cur]:return True
        self.visit[cur]=True
        for i in self.map[cur]:
            if self.dfs(i):return True
        self.pos[cur]=False
        self.result.append(cur)
        return False
