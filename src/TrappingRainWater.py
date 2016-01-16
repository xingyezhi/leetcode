__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def trap(self, height):
        if len(height)==0:
            return 0
        left=height[0]
        right=max(height)
        rightIndex=height.index(right)
        result=0
        for i in range(1,len(height)-1):
            if i>rightIndex:
                right=max(height[i:])
                rightIndex=height.index(right,i)
            if height[i]<left:
                result+=max(min(left,right)-height[i],0)
            else:
                left=height[i]
        return result

sol=Solution()
print sol.trap([]);

