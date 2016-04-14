<<<<<<< HEAD
__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def getSkyline(self, buildings):
        if len(buildings)==0:return []
        else:return self.divide(buildings,0,len(buildings))
    def divide(self,buildings,left,right):
        if right<=left:return []
        if right-left==1:
            return [[buildings[left][0],buildings[left][2]],[buildings[left][1],0]]
        mid=left+(right-left)/2
        leftSkyline=self.divide(buildings,left,mid)
        rightSkyline=self.divide(buildings,mid,right)
        if len(leftSkyline)==0 or len(rightSkyline)==0:
            return leftSkyline.extend(rightSkyline)
        leftindex,rightindex=len(leftSkyline)-1,0
        while leftindex>=0 and leftSkyline[leftindex][0]>rightSkyline[0][0]:
            leftindex-=1
        result=leftSkyline[:leftindex]
        h1=h2=0
        while leftindex<len(leftSkyline) and rightindex<len(rightSkyline):
            if leftSkyline[leftindex][0]<rightSkyline[rightindex][0]:
                x=leftSkyline[leftindex][0]
                h1=leftSkyline[leftindex][1]
                h=max(h1,h2)
                leftindex+=1
            elif leftSkyline[leftindex][0]>rightSkyline[rightindex][0]:
                x=rightSkyline[rightindex][0]
                h2=rightSkyline[rightindex][1]
                h=max(h1,h2)
                rightindex+=1
            else:
                x=leftSkyline[leftindex][0]
                h1=leftSkyline[leftindex][1]
                h2=rightSkyline[rightindex][1]
                h=max(h1,h2)
                leftindex+=1
                rightindex+=1
            if len(result)==0 or result[-1][1]!=h:
                result.append([x,h])
        result.extend(leftSkyline[leftindex:])
        result.extend(rightSkyline[rightindex:])
        #print left,right,result
        return result






# s="abc. ef e eg"
# print s.split()

t=[]
s=len(t) and t[-1]
print s
# sol=Solution()
# print sol.getSkyline([[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ])
=======
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
>>>>>>> origin/master
