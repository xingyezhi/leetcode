__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {integer[]} height
    # @return {integer}

    def maxArea(self, height):
        maxWater=0
        left=0
        right=len(height)-1
        while True:
            while left<right:
                    maxWater=max(maxWater,min(height[left],height[right])*(right-left))
                    if height[right]>height[left]:
                        leftheight=height[left]
                        left+=1
                        break
                    right-=1

            while left<right:
                if height[left]>leftheight:
                    break
                left+=1
            if left>=right:
                break
        return maxWater


sol=Solution()
print sol.maxArea([12,3,4,5])