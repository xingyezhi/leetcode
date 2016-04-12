# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
    def divide(self,buildings,left,right):
        if right-left==1:
            return [[buildings[left][0],buildings[left][2]]]
        elif right==left:
            return [[]]
        mid=left+(right-left)/2
        lresult=self.divide(buildings,left,mid+1)
        lresult=self.divide(buildings,mid+1,right)
