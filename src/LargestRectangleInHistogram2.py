__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def maximalRectangle(self, matrix):
        m=len(matrix)
        if m==0:return 0
        n=len(matrix[0])
        height=[int(i) for i in matrix[0]]
        print height
        result=self.largestRectangleArea(height)
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:
                    height[j]=0
            #print height
            result=max(result,self.largestRectangleArea(height))
        return result
    def largestRectangleArea(self, height):
        height.append(0)
        stack,result=[],0
        for i,v in enumerate(height):
            if len(stack)==0 or height[stack[-1]]<v:
                stack.append(i)
            else:
                while len(stack)>0 and height[stack[-1]]>v:
                    j=stack.pop()
                    result=max(result,(i if len(stack)==0 else (i-stack[-1]-1))*height[j])
                    #print result,j
                stack.append(i)
        height.pop()
        return result

sol=Solution()
print sol.maximalRectangle(
["10100","10111","11111","10010"]
)