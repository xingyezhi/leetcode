__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def largestRectangleArea(self, height):
        if len(height)==0:return 0
        stack=[(0,height[0])]
        result=height[0]
        for i,v in enumerate(height):
            if i==0:continue
            point=i
            while len(stack)!=0 and stack[-1][1]>=v:
                point=stack.pop()[0]
            stack.append((point,v))
            #print stack,result
            print stack
        return result

sol=Solution()
print sol.largestRectangleArea([2,1,5,6,2,3])