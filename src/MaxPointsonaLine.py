# coding=utf-8
__author__ = 'lenovo'

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        result=1
        for i in range(len(points)):
            maxi=1
            map={}
            same=0
            x1,y1=points[i].x,points[i].y
            for j in range(i+1,len(points)):
                x2,y2=points[j].x,points[j].y
                m,n=x2-x1,y2-y1
                if m==0 and n==0:
                    same+=1;continue
                k=self.gcd(m,n)
                m/=k;n/=k
                map.setdefault((m,n),1)
                map[(m,n)]+=1
                maxi=max(map[m,n],maxi)
            result=max(result,maxi+same)
        return result

    def gcd(self,a,b):
        if b==0:return a
        return self.gcd(b,a%b)

sol=Solution()
t=[(1,2),(2,4),(1,2),(3,6),(1,3),(1,4),(1,5),(1,6),(2,2)]
point=[Point(i[0],i[1]) for i in t]
print sol.maxPoints(point)